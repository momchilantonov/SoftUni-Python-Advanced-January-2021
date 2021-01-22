def word_filter(txt):
    result = [word for word in txt if len(word) % 2 == 0]
    return result


def print_result(txt):
    return [print(word) for word in txt]


words = input().split(" ")
print_result(word_filter(words))
