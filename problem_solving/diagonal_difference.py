def diagonalDifference(arr):
    sumofprimarydiagnol= 0 
    sumofsecondarydiagnol= 0
    for i in range(n):
        sumofprimarydiagnol += arr[i][i]
    for i in range(1, n+1):
        sumofsecondarydiagnol += arr[i-1][n-i]
    return abs(sumofprimarydiagnol - sumofsecondarydiagnol)

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = diagonalDifference(arr)
    
    print(result)
 
 
