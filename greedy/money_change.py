# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    d = [1, 5, 10]
    count = 0
    index = 2
    while money > 0:
        while d[index] >= money:
            money-=d[index]
            count+=1
        index+=1
    return count


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
