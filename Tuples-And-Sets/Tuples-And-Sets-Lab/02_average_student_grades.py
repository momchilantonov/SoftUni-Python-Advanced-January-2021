def input_line(num):
    res = {}
    for _ in range(num):
        name, grade = input().split(" ")
        grade = float(grade)
        if name not in res:
            res[name] = [grade]
        else:
            res[name].append(grade)
    return res


def take_average(students_data):
    for student, grade in students_data.items():
        avg = sum(grade) / len(grade)
        all_grades = ' '.join(map(lambda x: f'{x:.2f}', grade))
        print(f"{student} -> {all_grades} (avg: {avg:.2f})")


students = input_line(int(input()))
take_average(students)
