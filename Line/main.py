
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
line_lenght2 = length_calculate(1,0,2,0)  # length of second line

# Checking Lines are Equal or Not.
if line_lenght1 == line_lenght2:
    print("Lines are Equal")
elif line_lenght1 > line_lenght2:
    print("Line 1 is greater than Line 2")
else:
    print("Line 2 is greater than Line 1")
