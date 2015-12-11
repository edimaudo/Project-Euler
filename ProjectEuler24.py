#Lexicographic permutations
#Problem 24

import itertools
testlist = [0,1,2,3,4,5,6,7,8,9]
#testlist = [0,1,2]
output = list(itertools.permutations(testlist))

#print (output)

count = 0
for i in output:  
    if (count == 999999):
    #if (count == 1000000):
        print (i)
    count+=1
    




