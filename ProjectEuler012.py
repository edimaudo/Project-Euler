def tri_num(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
#print(tri_num(7))
#print(len(list(factors(28))))

for i in range(7,1000000):
    if len(list(factors(tri_num(i)))) > 500:
        print(tri_nums(i))


