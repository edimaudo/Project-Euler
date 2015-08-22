def self_power(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**i
        sum1 = str(sum)
    return sum1[-10:]


print(self_power(1000))
