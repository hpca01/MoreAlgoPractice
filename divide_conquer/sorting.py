# Uses python3
import sys
import random

def swap(array, swap_from:int, swap_to:int):
    array[swap_to], array[swap_from] = array[swap_from], array[swap_to]
    return


def partition3(a, l, r):
    #write your code here
    #first pass -> left of arr is pivot, find the right place for it first
    _right_mid = l
    for i in range(l + 1, r):
        if a[i]<=a[l]:
            swap(a, _right_mid+1, i)
            _right_mid += 1
    
    swap(a, _right_mid, l)
    
    _left_mid = l
    for i in range(l, _right_mid):
        if a[i] < a[_right_mid]:
            swap(a, _left_mid, i)
            _left_mid+=1
    return _left_mid, _right_mid

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r-1) # random int is inclusive...it can cause errors if it randomly selects EOL
    a[l], a[k] = a[k], a[l]
    #use partition3
    _left_mid, _right_mid = partition3(a, l, r)
    randomized_quick_sort(a, l, _left_mid) #python is inclusive
    randomized_quick_sort(a, _right_mid+1, r) #python is inclusive...


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n)
    for x in a:
        print(x, end=' ')