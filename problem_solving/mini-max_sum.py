def miniMaxSum(arr):
    max_min = []
    for i in arr:
        max_min.append(sum(arr) - i)
    print(f'{min(max_min)} {max(max_min)}')
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
 
 
