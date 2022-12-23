from math import sqrt
def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]
def len_func(data):
    len = 0
    len += sqrt(pow((data[1][0]-data[0][0]),2) + pow((data[1][1]-data[0][1]),2))
    return len

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    length = map(len_func, pairwise(pts))
    print(sum(list(length)))


