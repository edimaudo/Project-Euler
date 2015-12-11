#Project Euler 45

import math

def isPentagonal(n):
    output = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    if output == int(output):
        return True
    return False

result = 0
firsthex = 143
while (True):
    firsthex+=1
    result = firsthex * (2 * firsthex - 1);
    if (isPentagonal(result)):
        print (result)
        break;
    


    
