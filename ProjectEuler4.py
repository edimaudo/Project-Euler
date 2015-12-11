#Project Euler 4

#checks if a value is a palindrome
def ispalindrome(n):
    value = str(n)[::-1]
    if str(n) == value:
        return True
    return False

	
outputlist = []
for value1 in range(100,1000):
    for value2 in range(100,1000):
        newvalue = value2 * value1
        if ispalindrome(newvalue):
            outputlist.append(newvalue)
print (max(outputlist))

#print (ispalindrome(101))
