def appendAndDelete(s, t, k):
    count = 0
    
    for i in range(1,len(s)):
        if s[0:i] == t[0:i]:
            count += 1
    if len(s)-count+ len(t)-count == k:
        return 'Yes'
    elif len(s)-count+ len(t)-count < k and len(t) > len(s) and 2*len(s)+len(t)-count>k and k%(len(t)-count)!=0:
        return 'No'
    elif len(s)-count+ len(t)-count < k and k - (len(s)-count+ len(t)-count < k) %2 !=0:
        return 'Yes'
    
        
    return 'No'
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close() 
