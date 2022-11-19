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

task_1 =human_years_cat_years_dog_years(10)
print(task_1)
