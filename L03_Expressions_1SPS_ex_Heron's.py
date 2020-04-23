import math
side1 = 4
side2 = 7
side3 = 9
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print ("Length of sides: ", side1,', ',side2,' and ',side3, sep = "")
Length of sides: 4, 7 and 9
print ("Area:", area)