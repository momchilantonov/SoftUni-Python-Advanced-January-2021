seq = [0, 1]


def create_sequence(n):
    global seq
    if n == 0:
        return []
    elif n == 1:
        return [0]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1]+seq[-2])
    return seq


def locate(n):
    if n in seq:
        return f"The number -  {n} is at index {seq.index(n)}"
    else:
        return f"The number {n} is not in the sequence"
