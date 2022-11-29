

def base64_to_base10(char):
    """
    Функция для перевода из 64 системы в 10-ую
    :char: str
    :return: int
    """
    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    reversed_char = char[::-1]
    base10_view= 0
    for i,k in enumerate(reversed_char):
        base10_view+= pow(64,i) * int(base64.index(k))
    return base10_view

print(base64_to_base10('//'))


