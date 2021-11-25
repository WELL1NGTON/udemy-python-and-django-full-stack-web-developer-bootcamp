arr = [1, 2, 3, 4, 5, 6, 7]


def draw(ammount: int) -> list[int]:
    global arr

    total = len(arr)

    if total == 0:
        return []

    if total < ammount:
        ammount = total

    cards_drawn = arr[total - ammount: total]
    cards_remaining = arr[0:total - ammount]

    arr = cards_remaining

    return cards_drawn


print("drawn:", draw(2))
print("drawn:", draw(2))
print("drawn:", draw(9))
print("drawn:", draw(1))
print('remaining', arr)
