# Project Euler 44


import math

#checks if a number is pentagonal
def isPentagonal(n):
    output = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    if output == int(output):
        return True
    return False

templist = []
for i in range(2,10000):
    for j in range(2,10000):
        ival = (i*(3*i - 1))/2
        jval = (j*(3*j - 1))/2
        sumval = ival + jval
        diffval = jval - ival
        dval = abs(diffval)
        if diffval > 0:
            if isPentagonal(sumval) and isPentagonal(diffval):
                templist.append(dval)
print (min(templist))

        
