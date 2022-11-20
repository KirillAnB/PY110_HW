
def get_direction(direction, turn):
    """

    :param direction:
    :param turn:
    :return:
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



