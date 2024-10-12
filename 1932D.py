from itertools import combinations
from collections import deque


def can_beat(card1, card2, trump_suit):
    if card1[1] == card2[1]:
        if card1[1] == trump_suit:
            return card1 > card2
        return card1[0] == card2[0] or card1[0] > card2[0]
    elif card1[1] == trump_suit:
        return True
    return False


for _ in range(int(input())):
    n = int(input())
    trump_suit = input()
    cards = input().split()

    queue = deque([[cards, n * 2, []]])
    rez = []
    while queue:
        cards, left, path = queue.popleft()
        if left == 0:
            for plays in path:
                print(*plays)
            break
        for comb in list(combinations(cards, 2)):
            if can_beat(comb[1], comb[0], trump_suit):
                queue.append(
                    [
                        [i for i in cards if i not in comb],
                        left - 2,
                        path + [comb],
                    ]
                )
            elif can_beat(comb[0], comb[1], trump_suit):
                queue.append(
                    [
                        [i for i in cards if i not in comb],
                        left - 2,
                        path + [[comb[1], comb[0]]],
                    ]
                )
    else:
        print("IMPOSSIBLE")


"""
1
8
H
4S 3D 7H 3C 6D 2S 5S 9D 5C 4C 9C 8D 8H 9H 3E 7E
"""
