def getMoneySpent(keyboards, drives, b):
    x = [i+j for i in keyboards for j in drives]
    x.sort(reverse = True)
    for i in x:
        if b >= i:
            print(i)
            break
    if all([b < i for i in x]):
        print(-1)       
    
           

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    getMoneySpent(keyboards, drives, b)
 
