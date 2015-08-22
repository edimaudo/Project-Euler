def fib(n):
    a, b = 1, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

fistvalue=[]
for i in range(50,30000):
    x = list(fib(i))
    for i in range(len(x)):
        if len(str(x[i])) >= 1000 and len(str(x[i])) < 1001:
            firstvalue.append(i+1)
        print firstvalue[0]

#print list(fib(10))
#x = list(fib(30000))
#print (x)

###for i in range(len(x)):
##    if len(str(x[i])) >= 1000 and len(str(x[i])) < 1001:
##        print i+1


