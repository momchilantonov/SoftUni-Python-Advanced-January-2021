def input_lines():
    p_book = {}
    persons = []
    while True:
        cmd = input()
        if cmd.isdigit():
            for el in range(int(cmd)):
                persons.append(input())
            break
        name, num = cmd.split("-")
        p_book[name] = num

    return p_book, persons


def check_numbers(p_book, persons):
    for p in persons:
        if p not in p_book:
            print(f"Contact {p} does not exist.")
        else:
            print(f"{p} -> {p_book[p]}")


phonebook, people = input_lines()
check_numbers(phonebook, people)

