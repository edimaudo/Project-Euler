def sum_num_mult35(number):
    sum = 0
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return (sum)


print(sum_num_mult35(1000))
        
