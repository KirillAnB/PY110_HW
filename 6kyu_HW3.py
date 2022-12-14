import pprint


def sep_str(str_):
    list_ = str_1.split()
    height = len(max(list_, key = len))
    outter_list = []
    inner_list = []
    i=0
    for _ in range(height):
        for word in list_:
            try:
                inner_list.append(word[i])
            except:
                inner_list.append('')
        outter_list.append(inner_list)
        i+=1
        inner_list = []
    pprint.pprint(outter_list)
if __name__ == '__main__':
    str_1=("Just Live Life Man")
    sep_str(str_1)