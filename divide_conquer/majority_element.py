# python3
import sys

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def find_major(seq, l_bound, r_bound):

    if r_bound-l_bound <=2:
        return seq[l_bound]

    mid = l_bound + (r_bound - l_bound)//2

    l = find_major(seq, l_bound, mid)
    r = find_major(seq, mid, r_bound)

    counter_1, counter_2 = 0,0

    for number in seq[l_bound:r_bound]:
        if number == l:
            counter_1 +=1
        elif number == r:
            counter_2 +=1

    if counter_1 > (r_bound - l_bound)//2 and l != -1:
        return l
    elif counter_2 > (r_bound - l_bound)//2 and r != -1:
        return r
    else:
        return -1


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    value = find_major(elements, 0, len(elements))
    return value

def alternate_majority(elements):
    elements.sort()
    if len(elements) % 2 == 0:
        mid = len(elements)//2
        possible_majority = elements[mid]
        if possible_majority == elements[mid-1] and possible_majority == elements[mid+1]:
            return 1
        else:
            return -1
    elif len(elements) % 2 != 0 :
        mid = len(elements)//2
        possible_majority = elements[mid]
        if possible_majority == elements[mid-1] and possible_majority == elements[mid+1]:
            return 1
        else:
            return -1


# if __name__ == '__main__':
#     input_n = int(input())
#     input_elements = list(map(int, input().split()))
#     assert len(input_elements) == input_n
#     print(majority_element(input_elements))
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majority_element(a) != -1:
        print(1)
    else:
        print(0)
