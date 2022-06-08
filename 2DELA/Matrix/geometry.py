def line(lst):
    '''
    Line is a 4 pixel long figure

    ****

    lst shoudl be a lst with a tuple that contains to elements (x and y)
    lst outer layer needs to have 4 elements
    [(0, 1)]

    '''
    line = []
    for i in range(len(lst)):
        line.append(tuple((lst[i][0], lst[i][1], 1)))
    return line

#hei = [tuple((0, 4)), tuple((0, 5)), tuple((0, 6)), tuple((0, 7))]
#print(line(hei))