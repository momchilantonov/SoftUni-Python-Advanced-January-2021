def read_matrix(s):
    arr = [[int(x) for x in input().split(", ")] for _ in range(s)]
    return arr


def find_primary_diagonal(arr):
    pr_diagonal = [arr[i][i] for i in range(len(arr))]
    return pr_diagonal


def find_secondary_diagonal(arr):
    sec_diagonal = [arr[i][-i-1] for i in range(len(arr))]
    return sec_diagonal


def print_result(first_diagonal, second_diagonal):
    print(f"First diagonal: {', '.join(str(x) for x in first_diagonal)}. Sum: {sum(first_diagonal)}")
    print(f"Second diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")


size = int(input())
matrix = read_matrix(size)
primary_diagonal = find_primary_diagonal(matrix)
secondary_diagonal = find_secondary_diagonal(matrix)
print_result(primary_diagonal, secondary_diagonal)
