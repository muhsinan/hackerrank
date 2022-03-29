def getTotalX(a, b):
    x = 0
    for k in range(1,101):
        if all([k%i == 0 for i in a]):
            if all([j%k == 0 for j in b]):
                x += 1
    return x           
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    
    print(total)
 
 
