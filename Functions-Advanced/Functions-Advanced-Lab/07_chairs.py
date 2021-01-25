def combination(names, n, comb=[]):
    if len(comb) == n:
        print(", ".join(comb))
        return

    for i in range(len(names)):
        name = names[i]
        comb.append(name)
        combination(names[i+1:], n, comb)
        comb.pop()


input_names = input().split(", ")
num_comb = int(input())

combination(input_names, num_comb)
