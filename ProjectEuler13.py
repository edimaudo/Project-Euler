with open("/Users/edima/Documents/Project euler/Solved/peuler13.txt", "r") as fo: #update the filelocation
    result = []
    for line in fo.readlines():
        result.append(line.strip())
count = 0
sum = 0
for i in result:
    count= count + 1
    sum = sum + int(i)
    
print(str(sum)[0:10])
print(count)
    
    
    

