def utopianTree(n):
    h = 1
    while n>0:
        h *= 2
        n -= 1
        if n!=0:
            h += 1
            n -=1
    return h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
 
 
