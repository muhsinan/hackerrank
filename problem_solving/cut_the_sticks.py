def cutTheSticks(arr):
    numbers = [len(arr)]
    while arr:
        minofarr = min(arr)
        for i in range(len(arr)):
            arr[i] -= minofarr
        arr = list(filter(lambda a: a!=0, arr))
        numbers.append(len(arr)) if len(arr) != 0 else None
    for i in numbers:
        print(i, end = '\n')
            

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    cutTheSticks(arr)
 
 
