def migratoryBirds(arr):
    x = dict(Counter(arr))
    y = []
    for i in x.keys():
        if x[i] == max(x.values()):
            y.append(i)
    return min(y)    

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    
    print(result)
 
 
