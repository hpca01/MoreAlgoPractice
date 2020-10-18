# python3
from pprint import pprint


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    arr = matrix(first_sequence, second_sequence)
    return arr[len(second_sequence)][len(first_sequence)]

def matrix(seqA:tuple, seqB:tuple):
    # pre-pad with a non value, since input a sequence of ints a char will work just fine
    horizontal = ['\D'] + list(seqA)
    vertical = ['\D'] + list(seqB)
    i = len(horizontal)
    j = len(vertical)

    array = [[0]*i for _ in range(j)]
    #making an array with 0 filled in everywhere
    #  j i 0 1 2 3
    #  0
    #  1
    #  2
    #  3
    for row in range(1, j):
        for col in range(1, i):
            if vertical[row] == horizontal[col]:
                array[row][col] = 1 + array[row-1][col-1]
            else:
                array[row][col] = max(array[row-1][col], array[row][col-1])
    return array

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
