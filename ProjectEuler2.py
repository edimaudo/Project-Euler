def fib(n):
    a, b = 1, 2
    for _ in xrange(n):
        yield a
        a, b = b, a + b

#print list(fib(10))
x = list(fib(100))

sum = 0
for i in range(len(x) -1):
    if x[i] < 4000000 and x[i] % 2 == 0:
        sum += x[i]
print (sum)

