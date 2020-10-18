# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):

    if money == 0:
        return 0
    coins = [1, 3, 4]
    array = [-1] * (money + 1)
    for i in range(money+1):
        if i in coins:
            array[i] = 1
            continue
        combinations = [array[i-coin]+1 for coin in coins if i > coin]
        array[i] = min(combinations) if combinations else None

    return array[money]

if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
