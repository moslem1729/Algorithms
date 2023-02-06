bank_cards = []
while True:
    bank_card = input()
    if bank_card == "0000 0000 0000 0000":
        break
    else:
        bank_cards.append(bank_card)


def validator(bank_card):
    num = bank_card.replace(" ", "")

    odd_labeled = [int(num[i]) for i in range(0, 16, 2)]

    even_labeled = [int(num[i]) for i in range(1, 17, 2)]
    sum_of_odd = 0
    for n in odd_labeled:
        x = n * 2
        if x > 9:
            x = x - 9
        sum_of_odd = sum_of_odd + x
    sum_of_even = 0

    for n in even_labeled:
        sum_of_even = sum_of_even + n

    total = sum_of_even + sum_of_odd
    if total % 10 == 0:
        print("Yes")
    else:
        print("No")


for bank_card in bank_cards:
    validator(bank_card)
