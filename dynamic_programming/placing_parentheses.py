# Uses python3
import math
import pprint

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def MinAndMax(max_array, min_array, i, j, operators):
    min_val = math.inf
    max_val = -math.inf
    
    for k in range(i, j):
        a = evalt(max_array[i][k], max_array[k+1][j], operators[k])
        b = evalt(max_array[i][k], min_array[k+1][j], operators[k])
        c = evalt(min_array[i][k], max_array[k+1][j], operators[k])
        d = evalt(min_array[i][k], min_array[k+1][j], operators[k])
        min_val = min(min_val, a,b,c, d)
        max_val = max(max_val, a, b, c, d)
    
    return min_val, max_val

def get_maximum_value(dataset):
    #write your code here
    operators = []
    operands = []

    for i in dataset:
        if i in ["+", "-", "*"]:
            operators.append(i)
        else:
            operands.append(int(i))

    size_of_arr = len(operands)

    min_array = [[None for _ in range(size_of_arr)] for _ in range(size_of_arr)]
    max_array = [[None for _ in range(size_of_arr)] for _ in range(size_of_arr)]
    
    for i in range(size_of_arr):
        min_array[i][i] = operands[i]
        max_array[i][i] = operands[i]

    for s in range(1, size_of_arr):
        for i in range(size_of_arr - s):
            j = i+s
            min_array[i][j], max_array[i][j] = MinAndMax(max_array, min_array, i, j, operators)

    # pprint.pprint(min_array)
    # pprint.pprint(max_array)
    return max_array[0][size_of_arr-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
