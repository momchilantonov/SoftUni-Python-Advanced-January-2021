text = input()

s = []

for ch in text:
    s.append(ch)

result = ""

while s:
    result += s.pop()

print(result)
