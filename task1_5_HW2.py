from string import ascii_lowercase, ascii_uppercase, digits
from random import sample
def password_generator(simbols,n):
    while True:
        password = ''
        result = sample(simbols,n)
        yield password.join(result)


if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    str_1,str_2,str_3 = ascii_lowercase, ascii_uppercase, digits
    chars_list = str_1 + str_2 + str_3
    my_password = password_generator(chars_list,8)
    for _ in range(10):
        print(next(my_password))