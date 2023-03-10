from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError


valid_domains = {'com', 'bg', 'net', 'org'}

while True:
    line = input()
    if line == 'End':
        break

    email_parts = line.split('@')
    if len(email_parts) == 1:
        raise MustContainAtSymbolError('Email must contain @')

    if len(email_parts) != 2:
        raise MustContainAtSymbolError('Email must contain only one @ sign')
    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    domain_name_parts = domain_name.split('.')
    if len(domain_name_parts) < 2:
        raise InvalidDomainError('Domain must be one of the following : .com, .bg, .org, .net')
    domain = domain_name_parts[-1]
    if domain not in valid_domains:
        raise InvalidDomainError(f'Domain must be one of the following: .com, .bg, .org,\n'
                                 '.net')

    print('Email is valid')