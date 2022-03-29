def beautifulDays(i, j, k):
    thedays=0
    for a in range(i,j+1):
        if (int(str(a)[::-1]) - a) % k == 0:
            thedays += 1
    return thedays   

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
    
    print(result) 
