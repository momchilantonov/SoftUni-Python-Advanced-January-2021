def get_words_lengths():
    result = {word: len(word) for word in input().split(", ")}
    return result


def print_result():
    # result = [f"{text} -> {length}" for text, length in get_words_lengths().items()]
    # print(f"{', '.join(result)}")
    return print(*(f"{text} -> {length}" for text, length in get_words_lengths().items()), sep=", ", end="")


print_result()
