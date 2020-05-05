import math
side1 = 4
side2 = 7
side3 = 9

part1 = 4*(side1**2 * side2**2 + side1**2 * side3**2 + side2**2 * side3**2)
part2 = (side1**2 + side2**2 + side3**2)**2
area = 1/4 * math.sqrt(part1-part2)

print('Length of sides: ', side1,', ', side2, ' and ', side3, sep = '')
print('Area:', area)