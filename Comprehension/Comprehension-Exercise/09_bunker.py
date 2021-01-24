def create_the_bunker(cat_data):
    category = {cat: {'items': [], 'qty': [], 'qly': []} for cat in cat_data.split(", ")}

    return category


def fill_the_bunker(cat_data, num_fillings):
    for _ in range(num_fillings):
        category, item, item_data = input().split(" - ")
        quantity, quality = item_data.split(";")
        qty_text, qty_value = quantity.split(":")
        qty_value = int(qty_value)
        qly_text, qly_value = quality.split(":")
        qly_value = int(qly_value)

        cat_data[category]['items'].append(item)
        cat_data[category]['qty'].append(qty_value)
        cat_data[category]['qly'].append(qly_value)

    return cat_data


def count_items(bunker_data):
    num_items = sum([sum(val['qty']) for val in bunker_data.values()])

    # num_items = 0
    # for value in bunker_data.values():
    #     for val in value['qty']:
    #         num_items += val

    return num_items


def count_quality(bunker_data):
    average_qly = f"{(sum([sum(val['qly']) for val in bunker_data.values()]) / len(bunker_data)):.2f}"

    # total_qly = 0
    # for value in bunker_data.values():
    #     for val in value['qly']:
    #         total_qly += val
    #
    # average_qly = f"{total_qly / len(bunker_data):.2f}"

    return average_qly


def print_result(num_items, average_qly, bunker_data):
    print(f"Count of items: {num_items}")
    print(f"Average quality: {average_qly}")
    print(*[f"{key} -> {', '.join(value['items'])}" for key, value in bunker_data.items()], sep="\n")

    # for key, value in bunker_data.items():
    #     print(f"{key} -> {', '.join(value['items'])}")


categories_data = input()
number_of_fillings = int(input())

bunker = fill_the_bunker(create_the_bunker(categories_data), number_of_fillings)
number_of_items = count_items(bunker)
average_quality = count_quality(bunker)
print_result(number_of_items, average_quality, bunker)
