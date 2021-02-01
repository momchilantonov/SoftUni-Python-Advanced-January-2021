def read_tasks(tasks):
    return [int(task) for task in tasks.split(", ")]


def take_needed_tasks(tasks, task_idx):
    return [tasks[i] for i in range(len(tasks)) if tasks[i] <= tasks[task_idx]]


def looping_thru_tasks(tasks):
    total_clock_cycles = 0
    for task in tasks:
        total_clock_cycles += task
    return total_clock_cycles


task_numbers = input()
task_index = int(input())

all_tasks = read_tasks(task_numbers)
tasks_list = take_needed_tasks(all_tasks, task_index)

print(looping_thru_tasks(tasks_list))
