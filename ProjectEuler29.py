def int_com(a,b):
    valuelist=[]
    for i in range(2,a+1):
        for j in range(2,a+1): 
            valuelist.append(i**j)
    return len(list(set(valuelist)))

print(int_com(100,100))
        
