def draw_line(n):
    row = [str(i) for i in range(1, n+1)]
    print(" ".join(row))


def draw_triangle(n):
    for i in range(1, n+1):
        draw_line(i)
    for i in range(n-1, 0, -1):
        draw_line(i)
