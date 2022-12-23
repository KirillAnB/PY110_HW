
import string

plain_lower_list = string.ascii_lowercase
plain_upper_list = string.ascii_uppercase

def rot13_encryptor(str_):
    encripted_simbols = []
    message = ''
    for simbol in str_:
        if simbol in plain_lower_list:
            encripted_simbols.append(simbol_changer(plain_lower_list, simbol))
        elif simbol in plain_upper_list:
            encripted_simbols.append(simbol_changer(plain_upper_list, simbol))
        else:
            encripted_simbols.append(simbol)
    message = message.join(encripted_simbols)
    return message

def simbol_changer(list_, simbol, key = 13):
    new_index = list_.index(simbol) - key
    if new_index < 0 or new_index > 26:
        new_index = new_index % 26
    new_simbol = list_[new_index]
    return new_simbol

if __name__ == "__main__":
    text = 'Guvf vf zl svefg EBG13 rkprepvfr!'
    print(rot13_encryptor(text))