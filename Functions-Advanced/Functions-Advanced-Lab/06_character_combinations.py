# from itertools import permutations


def permute(text, curr_idx=0):
    if curr_idx == len(text):
        print("".join(text))
        return

    for i in range(curr_idx, len(text)):
        text[curr_idx], text[i] = text[i], text[curr_idx]
        permute(text, curr_idx+1)
        text[curr_idx], text[i] = text[i], text[curr_idx]


txt = list(input())

permute(txt)

# print(*[f"{''.join(el)}" for el in list(permutations(txt))], sep='\n')
