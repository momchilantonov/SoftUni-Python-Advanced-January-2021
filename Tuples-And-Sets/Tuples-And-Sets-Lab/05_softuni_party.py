def input_line(num):
    lines = set()
    for _ in range(num):
        lines.add(input())
    return lines


def input_until_cmd(end_cmd):
    lines = []
    while True:
        cmd = input()
        if cmd == end_cmd:
            break
        lines.append(cmd)
    return lines


def is_vip(guest):
    return guest[0].isdigit()


def separate(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return sorted(vip_guests), sorted(regular_guests)


def print_result(guests):
    print(len(guests))
    vip_guests, regular_guests = separate(guests)
    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)


reservations = input_line(int(input()))
guests_arrived = input_until_cmd("END")
guests_not_arrived = reservations.difference(guests_arrived)
print_result(guests_not_arrived)
