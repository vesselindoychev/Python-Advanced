class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
while True:
    line = input()
    if line == 'Stop':
        break

    text = line.split()
    sender = text[0]
    receiver = text[1]
    content = text[2]

    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(x) for x in input().split(', ')]

for i in indices:
    emails[i].send()

for mail in emails:
    print(mail.get_info())