#sums all numbers in a value
def sumoutput(arg1):
    total = 0
    newarg = str(arg1)
    for value in newarg:
        total += int(value)
    return total

output = []
for i in range(1,100):
    for j in range(1,100):
        value = j**i
        output.append(sumoutput(value))
print (max(output))





#print(sumoutput("1234"))
