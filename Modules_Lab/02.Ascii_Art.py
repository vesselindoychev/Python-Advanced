from pyfiglet import figlet_format


def print_art(text):
    art_text = figlet_format(text)
    return art_text


print(print_art('Hello World!'))
print(print_art('Python 3.8'))
