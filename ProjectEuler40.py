# Project Euler 40


beginvalue = ""
for value in range(1,1000001):
    beginvalue += str(value)
tenlist = [1,10,100,1000,10000,100000,1000000]

templist = []
for value in range(len(beginvalue)):
    if int(value) in tenlist:
        templist.append(beginvalue[int(value - 1)])
#print (templist)

multval = 1
for value in templist:
    multval *= int(value)
print (multval)



