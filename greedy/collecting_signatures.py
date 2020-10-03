# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    from operator import attrgetter
    segments.sort(key=lambda x: x.end)
    index = 0
    answer = []
    while index<len(segments):
        curr = segments[index]
        while index<len(segments)-1 and curr.end >= segments[index+1].start:
            index+=1
        answer.append(curr.end)
        index+=1
    return answer



if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
