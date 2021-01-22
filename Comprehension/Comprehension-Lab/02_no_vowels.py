# def clear_vowels():
#     vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I", ]
#     result = [ch for ch in input() if ch not in vowels]
#     return "".join(result)
#
#
# print(clear_vowels())


def clear_vowels():
    vowels = ["a", "o", "u", "e", "i"]
    result = [ch for ch in input() if ch.casefold() not in vowels]
    return "".join(result)


print(clear_vowels())
