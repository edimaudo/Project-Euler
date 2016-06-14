#Project Euler 35
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def rotate_number(num):
    num = str(num)
    output = []
    count = 0
    max_count = len(num)
    while count < max_count:
        if count == 0:
            output.append(int(num[count:count+1] + num[count+1:]))
        elif count < len(num) - 1:
            output.append(int(num[count:] + num[0:count]))
        else:
            output.append(int(num[count] + num[0:count]))
        count+=1
    return output

def check_prime_list(alist):
    output = [value for value in alist if is_prime(value)]
    if len(output) == len(alist):
        return True
    return False
        
def main():
    circular_prime_list = []
    for value in range(2,1000000):
        output = rotate_number(value)
        if check_prime_list(output):
            circular_prime_list.extend(output)
    print (len(set(circular_prime_list)))

    

if __name__ == '__main__':
    main()
