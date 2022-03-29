def squares(a, b):
    x = []
    for i in range(a,b+1):
        if str(i**(1/2))[-1] == '0':
            x.append(int(math.sqrt(i)))
            break
    for j in range(b,a-1,-1):
        if str(j**(1/2))[-1] == '0':
            x.append(int(math.sqrt(j)))
            break
    return len(range(x[0],x[1]+1)) if len(x) == 2 else 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
 
 
