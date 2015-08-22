def digit_sum(n):
    valuelist=[]
    value = 2**n
    value = str(value)
    for i in range(len(value)):
        valuelist.append(int(value[i]))
    return sum(valuelist)


#print (digit_sum(15))
print (digit_sum(1000))
