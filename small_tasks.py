import re
'''
1. Завершите код, который должен возвращать true, если данный объект представляет собой одну букву ASCII 
(нижний или верхний регистр), false в противном случае.

```python
assert is_letter("") == False
assert is_letter("X") == True
assert is_letter("a") == True
assert is_letter("7") == False
assert is_letter("_") == False
assert is_letter("ab") == False
assert is_letter("a\n") == False```
'''

def is_letter(char):
    pattern = re.compile(r'[A-Za-z]')
    result = pattern.search(char)
    return True if result else False
# print(is_letter("a"))
# assert is_letter("") == False
# assert is_letter("X") == True
# assert is_letter("a") == True
# assert is_letter("7") == False
# assert is_letter("_") == False
# assert is_letter("ab") == False
# assert is_letter("a\n") == False
def is_vovel(char):
    pattern = re.compile(r'[aeiouAEIOU]')
    result = pattern.search(char)
    return True if result else False
def six_bit_num(char):
    pattern = re.compile(r"^([0-9]|[1-5][0-9]|[6][0-3])$")
    result = pattern.search(char)
    return True if result else False
def eight_bit_num(char):
    pattern = re.compile(r"^([0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])$")
    result = pattern.search(char)
    return True if result else False
print(eight_bit_num('255'))