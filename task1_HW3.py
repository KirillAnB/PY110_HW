from string import ascii_lowercase, ascii_uppercase, digits
from random import sample
import json

OUTPUT_FILE1, OUTPUT_FILE2 = 'output_1.json', 'output_2.json'
str_1,str_2,str_3 = ascii_lowercase, ascii_uppercase, digits
chars_list = str_1 + str_2 + str_3

def random_list_gen(simbols , n):
    result = sample(simbols,n)
    return result


def task1(n):
    with open(OUTPUT_FILE1, "w") as of1,open(OUTPUT_FILE2, 'w') as of2:
        list_1 = random_list_gen(chars_list, n)
        list_2 = random_list_gen(chars_list, n)
        json.dump(list_1,of1)
        json.dump(list_2,of2)

def task2():
    with open(OUTPUT_FILE1, 'r') as if1, open(OUTPUT_FILE2, "r") as if2:
        readen_list1 = json.load(if1)
        readen_list2 = json.load(if2)
        print(f" Список из первого файла {readen_list1}, список из второго файла {readen_list2}.")

if __name__ == "__main__":
    task1(10)
    task2()