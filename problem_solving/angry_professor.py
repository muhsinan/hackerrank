def angryProfessor(k, a):
    ontime = 0
    for i in a:
        if i<=0:
            ontime+=1
    if k <= ontime:
        return 'NO'
    return 'YES'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        
        print(result)
 
 
