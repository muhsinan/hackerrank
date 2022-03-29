def sockMerchant(n, ar):
    x = 0
    y = dict(Counter(ar))
    for i in y.values():
        if i % 2 == 0:
            x += i/2
        else:
            x += (i-1)/2 
    return int(x)                
                        
            
 
if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
 
