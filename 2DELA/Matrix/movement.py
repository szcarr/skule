def shift(lst, direction, number):
    '''
    args expected is a list with tuples
    example = [(Value1, Value2, Value3)]

    direction is the direction you want to shift the figure
    direction should be an integer value
    direction value should be between 0-3

    0 = North
    1 = West
    2 = South
    3 = East

    Number is how many indexes you want to shift it by
    '''

    leftList = []
    for x in range(len(lst)):
        #if x == 0:
            #leftList.append(lst[0][0], lst[0][1], 0)
        if direction == 0:
            leftList.append(tuple((lst[x][0] - number, int(lst[x][1]), lst[x][2])))
        elif direction == 1:
            leftList.append(tuple((lst[x][0], int(lst[x][1] - number), lst[x][2])))
        elif direction == 2:
            leftList.append(tuple((lst[x][0] + number, int(lst[x][1]), lst[x][2])))
        elif direction == 3:
            leftList.append(tuple((lst[x][0], int(lst[x][1] + number), lst[x][2])))

    return leftList

