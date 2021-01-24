def read_heroes():
    names = {name: {"items": [], "cost": []} for name in input().split(", ")}
    return names


def collect_all_items(heroes_data):
    while True:
        command = input()
        if command == "End":
            break

        hero, item, cost = command.split("-")
        cost = int(cost)

        if item not in heroes_data[hero]["items"]:
            heroes_data[hero]["items"].append(item)
            heroes_data[hero]["cost"].append(cost)
    return heroes_data


def print_result(heroes_result):
    print(*[f"{key} -> Items: {len(val['items'])}, Cost: {sum(val['cost'])}"
            for key, val in heroes_result.items()], sep='\n')


heroes = read_heroes()
heroes_inventory = collect_all_items(heroes)
print_result(heroes_inventory)
