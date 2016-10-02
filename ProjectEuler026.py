def reciprocal_cycle(value):
    output_list = {}
    x,i = 1,0
    while x not in output_list:
        output_list[x] = i
        x = x * 10 % value
        i+=1
    return i - output_list[x]
    

def main():
    output = max(range(1,1000),key=reciprocal_cycle)
    print(str(output))


if __name__ == "__main__":
          main()
