#open filename and store in list

fileLocation = "/Users/edima/Desktop/p022_names.txt"
with open(fileLocation,"r") as f:
    word = f.read()
    newval = word.split('"')
    while ',' in newval:
	newval.remove(',')
    while '' in newval:
	newval.remove('')
f.close()

#sort list
newval.sort()

#print(newval)

alphabet = [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5], ['F', 6], ['G', 7], ['H', 8], ['I', 9], ['J', 10], ['K', 11], ['L', 12], ['M', 13], ['N', 14], ['O', 15], ['P', 16], ['Q', 17], ['R', 18], ['S', 19], ['T', 20], ['U', 21], ['V', 22], ['W', 23], ['X', 24], ['Y', 25], ['Z', 26]]

def wordsum(word, alphabet):
    sumvalue = 0
    for value in word:
        for letter in alphabet:
            if value == letter[0]:
                sumvalue += letter[1]
    return sumvalue

#print(newval)
#print(wordsum("COLIN", alphabet)) 
total = 0  
for value in newval:
    wordtotal = (newval.index(value) + 1) * wordsum(value, alphabet)
    total+=wordtotal
print(total)

    
