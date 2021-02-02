from pyfiglet import figlet_format


def print_art(msg):
    print(figlet_format(msg, font="isometric1"))


print_art(input())
