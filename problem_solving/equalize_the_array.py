def equalizeArray(arr):
    count = 0
    for i in arr:
        if arr.count(i)>count:
            count = arr.count(i)
    return len(arr)-count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
 
 
