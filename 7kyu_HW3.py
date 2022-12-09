input_str = "How can mirrors be real if our eyes aren't real"


def str_capitaliser(str_):
    cap_list = [word for word in map(str.capitalize, str_.split())]
    output_str = ' '.join(cap_list)

    return output_str


if __name__ == '__main__':
    output_str = str_capitaliser(input_str)
    print(output_str)
