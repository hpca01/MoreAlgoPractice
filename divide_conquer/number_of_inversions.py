# python3

from itertools import combinations


def merge(array1, array2):
    arr_out = []
    left_offset = 0
    right_offset = 0
    inv = 0
    for _ in range(0, len(array1) + len(array2)):
        if left_offset == len(array1):
            for each in array2[right_offset:]:
                arr_out.append(each)
            break
        elif right_offset == len(array2):
            for each in array1[left_offset:]:
                arr_out.append(each)
            break
        elif array1[left_offset] <= array2[right_offset]:
            arr_out.append(array1[left_offset])
            left_offset += 1
        else:
            arr_out.append(array2[right_offset])
            right_offset += 1
            inv += len(array1) - left_offset
    return arr_out, inv

def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    # implement a divide and conquer approach
    def wrapper(a):
        if len(a) == 1:
            return a, 0

        mid = len(a)//2

        left_arr, inv_l = wrapper(a[0:mid])
        right_arr, inv_r = wrapper(a[mid:])

        results, inv_count = merge(left_arr, right_arr)

        return results, (inv_count + inv_l + inv_r)

    _, inv = wrapper(a)

    return inv


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
    # elements = [1] * 10
    # print(len(elements))
    # print(compute_inversions(elements))
