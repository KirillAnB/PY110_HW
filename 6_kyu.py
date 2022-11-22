import string

def encryptor(key, plain_text):
    """

    :param key: int ключ смещения
    :param plain_text: str текст для шифровки
    :return: str зашифрованный текст
    """
    plain_lower_list = string.ascii_lowercase
    plain_upper_list = string.ascii_uppercase
    encripted_simbols = []
    message = ''
    for simbol in plain_text:
        if simbol in plain_lower_list:
            new_index = plain_lower_list.index(simbol) + key
            if new_index < 0 or new_index > 26:
                new_index = new_index % 26
            new_simbol = plain_lower_list[new_index]
            encripted_simbols.append(new_simbol)
        elif simbol in plain_upper_list:
            new_index = plain_upper_list.index(simbol) + key
            if new_index < 0 or new_index > 26:
                new_index = new_index % 26
            new_simbol = plain_upper_list[new_index]
            encripted_simbols.append(new_simbol)
        else:
            encripted_simbols.append(simbol)
    message = message.join(encripted_simbols)
    return message
my_text = encryptor(27, 'Whoopi Goldberg')
print(my_text)
