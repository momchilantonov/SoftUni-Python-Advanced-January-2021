from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(el) for el in input().split(" ")]
locks = deque(int(el) for el in input().split(" "))
intelligence = int(input())
bullet_counter = 0
reload_counter = 0


def reload(counter):
    if bullets and counter == barrel_size:
        print("Reloading!")
        counter = 0
        return counter
    return counter


def shoot():
    if shooting_gallery["lock"] >= shooting_gallery["bullet"]:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(shooting_gallery["lock"])


while bullets and locks:
    shooting_gallery = {"lock": locks.popleft(), "bullet": bullets.pop()}
    shoot()
    bullet_counter += 1
    reload_counter += 1
    reload_counter = reload(reload_counter)

if not len(locks) == 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence-(bullet_counter*bullet_price)}")

# from collections import deque
#
# bullet_price = int(input())
# barrel_size = int(input())
# bullets = [int(el) for el in input().split(" ")]
# locks = deque(int(el) for el in input().split(" "))
# intelligence = int(input())
# bullet_counter = 0
# reload_counter = 0
#
# while bullets and locks:
#     checker = {"lock": locks.popleft(), "bullet": bullets.pop()}
#     if checker["lock"] >= checker["bullet"]:
#         print("Bang!")
#         bullet_counter += 1
#         reload_counter += 1
#         if bullets and reload_counter == barrel_size:
#             reload_counter = 0
#             print("Reloading!")
#     else:
#         print("Ping!")
#         bullet_counter += 1
#         reload_counter += 1
#         if bullets and reload_counter == barrel_size:
#             print("Reloading!")
#             reload_counter = 0
#         locks.appendleft(checker["lock"])
#
# if not len(locks) == 0:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# else:
#     print(f"{len(bullets)} bullets left. Earned ${intelligence-(bullet_counter*bullet_price)}")
