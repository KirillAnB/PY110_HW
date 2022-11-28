if __name__ == "__main__":
    list_=['a','b','c','d','e','f'] #Тестовый список
    #Образец поведения функции enumerate, который пытаемся реализовать:
    # item = enumerate(list_)
    # print(next(item))
    # print(next(item))
    def my_enumarate(l):
        """
        Реализуем функцию enumerate при помощи функции zip

        :param l: итерируемый обьект
        :return: итератор
        """
        iterator_ = zip(range(len(l)),l)
        return iterator_

    item = my_enumarate(list_)
    print(next(item))
    print(next(item))
