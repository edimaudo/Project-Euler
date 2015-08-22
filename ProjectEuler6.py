def sumsqu_natnum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return (sum)


def squsum_natnum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return (sum**2)

print(squsum_natnum(100)- sumsqu_natnum(100)) 
