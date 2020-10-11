# python3
import sys

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    left = 0
    right = len(keys)-1
    index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if keys[mid] == query:
            return mid
        elif keys[mid] < query:
            left = mid + 1
        elif keys[mid] > query:
            right = mid - 1
    return index


# if __name__ == '__main__':
#     input_keys = list(map(int, input().split()))[1:]
#     input_queries = list(map(int, input().split()))[1:]

#     for q in input_queries:
#         print(binary_search(input_keys, q), end=' ')
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')