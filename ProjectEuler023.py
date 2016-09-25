def sum_divisor(alist):
    return sum(alist)

def proper_divisor(number):
    return [value for value in range(1,number) if number % value == 0]

max_number, total = 20162, 0
set_data = set()

for value in range(1, max_number):
    if sum_divisor(proper_divisor(value)) > value:
        set_data.add(value)
    if not any( (value-item in set_data) for item in set_data):
        total += value
 
print total