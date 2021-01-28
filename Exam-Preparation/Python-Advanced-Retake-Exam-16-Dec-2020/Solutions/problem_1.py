from collections import deque


def read_sequences():
    return [int(x) for x in input().split(" ") if int(x) > 0]


def special_case(person, seq):
    return person % 25 == 0 and len(seq) > 0


def is_match(male, female):
    return male == female


def has_point(male):
    return male-2 > 0


def search_matches(males, females):
    matches_count = 0
    females = deque(females)
    while males and females:
        male = males.pop()
        if special_case(male, males):
            males.pop()
            continue
        female = females.popleft()
        if special_case(female, females):
            females.popleft()
            males.append(male)
            continue
        if is_match(male, female):
            matches_count += 1
            continue
        else:
            if has_point(male):
                males.append(male-2)
    return matches_count, males, females


def print_matches_result(match_counter, males_left, females_left):
    print(f"Matches: {match_counter}")
    if males_left:
        print(f"Males left: {', '.join(str(male) for male in males_left[::-1])}")
    else:
        print("Males left: none")
    if females_left:
        print(f"Females left: {', '.join(str(female) for female in females_left)}")
    else:
        print("Females left: none")


males_seq = read_sequences()
females_seq = read_sequences()
matches, total_males, total_females = search_matches(males_seq, females_seq)
print_matches_result(matches, total_males, total_females)
