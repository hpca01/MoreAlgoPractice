# python3

#                                 n  L    x
def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    index = 0
    refills = 0
    stops.insert(0, 0)
    stops.append(d)
    print("Distance {} Miles per Tank {} Stops {}".format(d, m, stops))
    while index < len(stops)-1:
        last_refill = index
        while ((index < len(stops)-1) and (stops[index + 1] - stops[last_refill] <= m)):
            index += 1
        if last_refill == index:
            return -1
        if index < len(stops)-1:
            refills += 1
    return refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
