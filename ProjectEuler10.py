def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n==2:
        return True
    if not n & 1:
        return False
    for x in range(3,int(n**0.5)+1,2):
        if n % x == 0:
            return False
    return True

sum = 0
for i in range(1,2000000):
    if is_prime(i) == True:
        sum+=i
print(sum)
