def viralAdvertising(n):
    shared = 6
    liked = 2
    while n>1:
        liked += math.floor(shared/2)
        shared = math.floor(shared/2)*3
        n -= 1
    return liked
    

if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)
    
    print(result)
 
 
