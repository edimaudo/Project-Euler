#Project Euler 14
# Longest Collatz sequence

from operator import itemgetter

def checkchain(arg):
    finallist = []
    outputlist = []
    n = arg
    while (n != 1):
        if n % 2 == 0:
            n = n/2
            outputlist.append(n)
        elif n % 2 != 0:
            n = 1 + (3*n)
            outputlist.append(n)
    return ([arg,len(outputlist) + 1])

#1000000
#print (checkchain(13))
finaloutput = []
finaloutputsorted = []
for value in range(1,1000000):
    finaloutput.append(checkchain(value))
finaloutputsorted = sorted(finaloutput, key=itemgetter(1))
print(finaloutputsorted[len(finaloutputsorted)-1])


