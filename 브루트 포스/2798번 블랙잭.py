import itertools

N, M = map(int, input().split())
card_list = list(itertools.combinations(map(int, input().split()), 3))
blackjack_list = []
blackjack = 0

for i in range(len(card_list)):
    blackjack = sum(card_list[i])
    if blackjack <= M:
        blackjack_list.append(blackjack)

print(max(blackjack_list))