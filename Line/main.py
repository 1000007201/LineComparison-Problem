
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
line_lenght1 = length_calculate(2,0,1,3)  # length of first line
line_lenght2 = length_calculate(1,0,2,3)  # length of second line

# Checking Lines are Equal or Not.
print("Lines are Equal") if line_lenght1 == line_lenght2 else print("Lines are not Equal")