def saveThePrisoner(n, m, s):
    m = m - (m//n)*n if m>n else m
    if m == 0:
        m = n
    return s+m-1 if s+m-1 <= n else s+m-1-n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
 
