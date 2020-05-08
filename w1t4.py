ounces = 1571
pints_in_gallon = 8
ounces_in_pint = 16

#gallons
gallon = pints_in_gallon * ounces_in_pint
ounces_in_gallon = ounces // gallon

#ounces
ounces_in_ounces = ounces % ounces_in_pint

#pints
ounces_in_pints = ounces % ounces_in_ounces

print(ounces,'ounces is equivalent to:')
print(ounces_in_gallon, 'gallons,', ounces_in_pints, 'pints and', ounces_in_ounces, 'ounces')
