def expon(num,base):
    while True:
        yield num
        num *= base


if __name__ == "__main__":
    i = expon(10, 2)
    for _ in range(10):
        print(next(i))
