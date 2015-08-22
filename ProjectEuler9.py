for c in range(1,1000):
    for b in range(1,c):
        for a in range(1,b):
            if a+b+c == 1000 and b**2 + a**2 == c**2:
                print (a,b,c,a*b*c)
