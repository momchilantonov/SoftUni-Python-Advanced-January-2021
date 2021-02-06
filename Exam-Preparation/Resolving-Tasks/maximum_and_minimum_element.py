def push(seq, n):
    seq.append(n)
    return seq


def delete(seq):
    if seq:
        seq.pop()
        return seq
    return seq


def print_max(seq):
    if seq:
        print(max(seq))


def print_min(seq):
    if seq:
        print(min(seq))


def loop():
    sequence = []
    for i in range(int(input())):
        command = input().split()
        action = command[0]

        if action == "1":
            num = command[1]
            num = int(num)
            sequence = push(sequence, num)
        elif action == "2":
            sequence = delete(sequence)
        elif action == "3":
            print_max(sequence)
        elif action == "4":
            print_min(sequence)
    return sequence


def print_seq(seq):
    new_seq = []
    while seq:
        new_seq.append(seq.pop())
    print(", ".join(str(x) for x in new_seq))


result = loop()
print_seq(result)
