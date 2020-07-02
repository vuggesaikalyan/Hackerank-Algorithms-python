import sys


def happy_ladybugs(bugs):
    mappings = {}
    free_cell = False
    happy = True

    for i, bug in enumerate(bugs):
        if i == 0 and i + 1 < len(bugs):
            happy = bug == bugs[i + 1]
        elif i == len(bugs) - 1:
            happy = bugs[i - 1] == bug and happy
        else:
            happy = happy and (bugs[i - 1] == bug or bugs[i + 1] == bug)

        # count the bugs
        if bug == '_':
            free_cell = True
        elif bug in mappings:
            mappings[bug] += 1
        else:
            mappings[bug] = 1

    singles = 0

    for bug, count in mappings.items():
        if count == 1:
            singles += 1

    if singles > 0:
        return 'NO'

    if not free_cell:
        return 'YES' if happy else 'NO'

    return 'YES'


games = int(input())

for _ in range(games):
    n = int(input())
    b = input()

    print(happy_ladybugs(b))
