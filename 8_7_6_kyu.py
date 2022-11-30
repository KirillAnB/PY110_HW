import string

# Калькулятор челове-кошка-собака
def human_years_cat_years_dog_years(years:int)-> list:
    """
    Функция принимает целое число и возвращает спиов из трех целых чисел
    :param years: принимает целое число
    :return: возвращает список целых чисел
    """
    human_years = years
    cat_years,dog_years = 0,0
    years_list = []
    for count in range(1,years+1):
        if count == 1:
            cat_years += 15
            dog_years += 15
        elif count == 2:
            cat_years +=9
            dog_years +=9
        elif count > 2:
            cat_years +=4
            dog_years +=5
    years_list = [human_years,cat_years,dog_years]
    return  years_list

assert human_years_cat_years_dog_years(1) == [1,15,15]
assert human_years_cat_years_dog_years(2) == [2,24,24]
assert human_years_cat_years_dog_years(10) == [10,56,64]


# Компас
def get_direction(direction, turn):
    """ Функция получения нового направления

    :param direction: str Текущее напрвление
    :param turn: int Поворот кратный 45 в интервале -1080 +1080
    :return: str Новое напрвление
    """
    directions = {
            'N': 0, 'NE': 45, 'E':90,
            'SE': 135, 'S':180, 'SW': 225,
            'W': 270, 'NW': 315, }
    current_direction = directions[direction]
    new_direction_digit = (current_direction + turn) % 360
    for k,v in directions.items():
        if v == new_direction_digit:
            return k

assert get_direction("S", 180) == "N"
assert get_direction("SE", -45) == "E"
assert get_direction("W", 495) == "NE"

# Caesar Cipher
def encryptor(key, plain_text):
    """Основная функция-шифровальщик

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
            encripted_simbols.append(simbol_chager(plain_lower_list, key, simbol))
        elif simbol in plain_upper_list:
            encripted_simbols.append(simbol_chager(plain_upper_list, key, simbol))
        else:
            encripted_simbols.append(simbol)
    message = message.join(encripted_simbols)
    return message

def simbol_chager(lower_list, index_chage, char):
    """ Функция для получения нового значения символа

    :param lower_list: list список символов без смещения
    :param index_chage: int ключ смещения
    :param char: str новый символ
    :return: str
    """
    new_index = lower_list.index(char) + index_chage
    if new_index < 0 or new_index > 26:
        new_index = new_index % 26
    new_simbol = lower_list[new_index]
    return new_simbol

assert encryptor(13, '') == ''
assert encryptor(13, 'Caesar Cipher') == 'Pnrfne Pvcure'
assert encryptor(-5, 'Hello World!') == 'Czggj Rjmgy!'
assert encryptor(27, 'Whoopi Goldberg') == 'Xippqj Hpmecfsh'