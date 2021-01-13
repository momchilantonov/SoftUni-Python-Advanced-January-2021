expression = input()

s = []

for i in range(len(expression)):
    if expression[i] == "(":
        s.append(i)
    elif expression[i] == ")":
        j = s.pop()
        print(expression[j:i+1])
