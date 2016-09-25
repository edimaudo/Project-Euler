def sum_divisor(alist):
    total = 0
    for value in alist:
        total+=value
    return total

def proper_divisor(number):
    alist = [value for value in range(1,number) if number % value == 0]
    return(alist)

def generate_amicable(number):
    return sum_divisor(proper_divisor(number))

def main():
    total = 0
    alist = []
    for value in range(1,10000):
        check_val = generate_amicable(value)
        if value == generate_amicable(check_val) and value != check_val:
            total+=value
            alist.append(value)
    print(total,alist)
    
main()
    

