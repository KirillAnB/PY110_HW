from more_itertools import pairwise
def task(str_):
    return pairwise(str_)


if __name__ == "__main__":
    my_str = 'ABCDEFG'
    pair = task(my_str)
    print(next(pair))
    print(next(pair))

