def birthday(s, d, m):
    x = 0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            x += 1
    return x        

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    
    print(result)
 
 
