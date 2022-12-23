def my_decorator(fn):
    def wrapper(*args):
        for i in args:
            if not isinstance(i,int):
                raise Exception(f"Check your args, {i}")
        print("Все параметры в порядке")
        result = fn(*args)
        print("Функция отработала")
        return result
    return wrapper

@my_decorator
def my_func(a,b,c):
    my_sum = a + b + c
    return my_sum

if __name__ == "__main__":
    my_func(1,'2',3)
