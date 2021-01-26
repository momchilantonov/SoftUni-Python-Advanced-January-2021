def concatenate(*args):
    result = ""
    for txt in args:
        result += txt
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))