from collections import deque

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120


def read_bomb_effects():
    return deque(int(x) for x in input().split(", "))


def read_bomb_casings():
    return [int(x) for x in input().split(", ")]


def mix_bombs(effects, casings):
    datura_counter = 0
    cherry_counter = 0
    smoke_decoy_counter = 0
    while True:
        is_fill_bomb_pouch = datura_counter >= 3 and cherry_counter >= 3 and smoke_decoy_counter >= 3
        if not effects or not casings or is_fill_bomb_pouch:
            break
        current_effect = effects.popleft()
        current_casing = casings.pop()
        if current_effect+current_casing == DATURA_BOMBS:
            datura_counter += 1
        elif current_effect+current_casing == CHERRY_BOMBS:
            cherry_counter += 1
        elif current_effect+current_casing == SMOKE_DECOY_BOMBS:
            smoke_decoy_counter += 1
        else:
            current_casing -= 5
            casings.append(current_casing)
            effects.appendleft(current_effect)
    if is_fill_bomb_pouch:
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")
    if not effects:
        print("Bomb Effects: empty")
    else:
        print(f"Bomb Effects: {', '.join(str(x) for x in effects)}")
    if not casings:
        print("Bomb Casings: empty")
    else:
        print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
    print(f"Cherry Bombs: {cherry_counter}")
    print(f"Datura Bombs: {datura_counter}")
    print(f"Smoke Decoy Bombs: {smoke_decoy_counter}")


bomb_effects = read_bomb_effects()
bomb_casings = read_bomb_casings()
mix_bombs(bomb_effects, bomb_casings)
