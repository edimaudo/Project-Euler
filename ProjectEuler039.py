#Project Euler 39
#Integer right triangles
import math
from operator import itemgetter

def check_perimeter(value):
    countval = 0
    for a in range(1,int(value/3)):
        b = (value**2 - (2*value*a))/(2*(value - a))
        c = math.sqrt(a**2 + b**2)
        if int(a) + int(b) + int(c) == value:
            countval += 1
    return countval


finallist = []
for i in range(1,1001):
    finallist.append([i,check_perimeter(i)])
print(sorted(finallist, key = itemgetter(1))[len(finallist) - 1][0])