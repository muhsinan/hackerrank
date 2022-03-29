def permutationEquation(p):
    p.insert(0,'')
    x=[]
    for i in range(1,n+1):
        x.append((i, p[p[i]]))
    x.sort(key=lambda x:x[1])
    for a,b in x:
        print(a, end='\n')
if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    permutationEquation(p)
 
 
