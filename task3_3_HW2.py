
def my_decorator(fn):
    def my_wrapper(*args, **kwargs):
        print("Проверяем аргументы функции")
        for a in args:
            try:
                iterable = iter(a)
            except:
                print(f"{a} не является итерируемым")
        for k,v in kwargs.items():
            try:
                iterable = iter(v)
            except:
                print(f"{v} не является итерируемым")
        print("Проверка аргументов завершена")
        result = fn(*args, **kwargs)
        return result
    return my_wrapper

@my_decorator
def my_func(*args,**kwargs):
    pass
# from collections.abc import Iterable
#
# def my_decorator(fn):
#     def my_wrapper(*args, **kwargs):
#         print("Проверяем аргументы функции")
#         for a in args:
#             if not isinstance(a, Iterable):
#                 raise TypeError(f" Объект {a} в {args} не является итератором")
#         for k,v in kwargs.items():
#             if not isinstance(v,Iterable):
#                 raise TypeError(f"Объект {v} в {kwargs} не является итератором")
#         print("Аргументы были проверены")
#         result = fn(*args, **kwargs)
#         return result
#     return my_wrapper
#
# @my_decorator
# def my_func(*args,**kwargs):
#     pass

if __name__ == "__main__":
    my_func(1, 2, x=[1,2])