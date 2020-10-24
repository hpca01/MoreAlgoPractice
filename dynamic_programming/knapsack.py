# Uses python3
import sys
import pprint

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def op_weight(W, w):
    """
    Parameters
    1. W - a positive int
    2. w - an integer array of values less than W
    """

    value = [([0]*(W+1)) for _ in range(len(w)+1)]
    # pprint.pprint(value)
    # print('\n')
    for row in range(1, len(w)+1):
        for column in range(1, W+1):
            value[row][column] = value[row-1][column]
            #w = w[column-1] because array is 0 indexed but value table is 1 indexed
            #w sub i = w[row-1] because array is 0 indexed but value table is 1 indexed
            if w[row-1] <= column:
                val = value[row-1][column-w[row-1]] + w[row-1]
                if val > value[row][column]:
                    value[row][column] = val
        # print('\n')
        # pprint.pprint(value)

    return value[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(op_weight(W, w))
    
