Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> side1 = 4
>>> side2 = 7
>>> side3 = 9
>>> s = (side1 + side2 + side3) / 2
>>> area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
>>> print ("Length of sides: ", side1,', ',side2,' and ',side3, sep = "")
Length of sides: 4, 7 and 9
>>> print ("Area:", area)