import random

def Naive(cards):
    count = {}
    for i in range(1000000):
        s_cards = cards[:]
        for j in range(len(cards)):
            n = random.randint(0, len(cards) - 1)
            s_cards[j], s_cards[n] = s_cards[n], s_cards[j]
        if tuple(s_cards) in count.keys():
            count[tuple(s_cards)] += 1
        else:
            count[tuple(s_cards)] = 1
    return count

def Fisher_Yates(cards):
    count = {}
    for i in range(1000000):
        s_cards = cards[:]
        for j in range(len(cards)-1, 0, -1):
            n = random.randint(0, j)
            s_cards[j], s_cards[n] = s_cards[n], s_cards[j]
        if tuple(s_cards) in count.keys():
            count[tuple(s_cards)] += 1
        else:
            count[tuple(s_cards)] = 1
    return count

cards = [1, 2, 3, 4]
print('Naive:')
naive_count = Naive(cards)
for a, b in naive_count.items():
    print(f'{a} : {b}')
print('-------------------------------')
print('Fisher-Yates:')
FY_count = Fisher_Yates(cards)
for a, b in FY_count.items():
    print(f'{a} : {b}')