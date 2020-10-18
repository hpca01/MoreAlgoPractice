# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def correct_sol(n):
    return print_seq(n, min_ops(n))

def min_ops(n):
    ops = [0]*(n+1)
    
    for i in range(2, n+1):
        min1, min2, min3 = [ops[i-1]] * 3
        
        if i % 2 == 0:
            min2 = ops[i//2]
        if i % 3 == 0:
            min3 = ops[i//3]
        
        correct_min = min(min1, min2, min3)

        ops[i] = correct_min+1    
    return ops

def print_seq(n, ops):
    if n == 1:
        return [1]
    seq = []
    while n > 0:
        seq.append(n)
        if n % 3 == 0 and n % 2 == 0:
            n = n//3
        elif n % 3 != 0 and n % 2 != 0:
            n = n-1
        elif n % 3 == 0:
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n//3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n//2
    return reversed(seq)

input = sys.stdin.read()
n = int(input)
sequence = list(correct_sol(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
