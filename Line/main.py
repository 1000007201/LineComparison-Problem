
def length_calculate(x1,y1,x2,y2):
    '''

    :param x1: x cordinate of 1st point
    :param y1: y cordinate of 1st point
    :param x2: x cordinate of 2nd point
    :param y2: y cordinate of 2nd point
    :return: distance between cordinates
    '''
    return (((x2-x1)**2)+((y2-y1)**2))**(1/2)

# calling length_calculate function.
line_lenght = length_calculate(0,0,1,0)
# Printing length of line:
print(f"Length of Line is: {line_lenght}")