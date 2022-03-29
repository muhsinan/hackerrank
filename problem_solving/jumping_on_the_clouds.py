def jumpingOnClouds(c, k):
    health = 100
    position = k
    while (position)%len(c)!=0:
        if c[(position)%len(c)] == 0:
            health -= 1
        else:
            health -= 3
        position += k
    return health-1 if c[0] == 0 else health-3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

 
