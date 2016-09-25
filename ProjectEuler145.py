import math

def reverse_number(num):
	str_num = str(num)
	reverse_num = str_num[::-1]
	return int(reverse_num)

def check_odd(num):
	count = 0
	str_num = str(num)
	for value in str_num:
		if int(value) % 2 != 0:
			count+=1
	if count == len(str_num):
		return True
	return False


def main():
        count = 0
        for value in range(1,1000000000):
                if value % 10 == 0:
                        pass
                else:
                        if check_odd(value + reverse_number(value)):
                                count+=1
        print(count)


main()
