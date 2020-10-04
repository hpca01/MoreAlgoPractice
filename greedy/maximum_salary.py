# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_bigger(num, other_num):
    return int(str(num) + str(other_num)) >= int(str(other_num) + str(num))

def largest_number(numbers):
    nums = numbers.copy()
    output = []
    while len(nums) > 0:
        highest = 0
        for number in nums:
            if is_bigger(number, highest):
                highest = number
        output.append(highest)
        nums.remove(highest)
    return int("".join(map(str, output)))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
