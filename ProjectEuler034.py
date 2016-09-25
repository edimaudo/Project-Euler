# Project Euler 34

#Digit factorials

import math
def get_curious_number(value):
    sumval = 0
    newval = str(value)
    for i in newval:
        sumval += math.factorial(int(i))
    return int(sumval)

templist = []
for i in range(3,10000000):
    if get_curious_number(i) == i:
        templist.append(i)
print (sum(templist))