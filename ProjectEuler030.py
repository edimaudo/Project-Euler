#project Euler 30 - Digit fifth powers


import math

def generate_fifth_power(value):
    templist = []
    sumval = 0
    for i in list(str(value)):
        templist.append(int(i))
    for j in templist:
        sumval += math.pow(j,5)
    return sumval


output_list = []
for i in range (1,1000000):
    if i == generate_fifth_power(i) and generate_fifth_power(i) !=1:
        output_list.append(i)
print(sum(output_list))


    
