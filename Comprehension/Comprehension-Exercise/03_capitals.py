def get_capitals():
    capitals = {country: city for country, city in zip(input().split(", "), input().split(", "))}
    return capitals


def print_result():
    # for country, city in get_capitals().items():
    #     print(f"{country} -> {city}")
    return [print(f"{country} -> {city}") for country, city in get_capitals().items()]


print_result()
