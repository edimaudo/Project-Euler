import math

def factdigitsum(n):
    valuelist=[]
    value = math.factorial(n)
    value = str(value)
    for i in  value:
        valuelist.append(int(i))
    return sum(valuelist)
 

print(factdigitsum(100))
