def repeatedString(s, n):
    numberofa = len(list(filter(lambda m: m == 'a', list(s))))
    return (n//len(s))*numberofa + len(list(filter(lambda m: m == 'a', list(s[0:n%len(s)]))))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
 
 
