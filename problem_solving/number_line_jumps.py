def kangaroo(x1, v1, x2, v2):
    t = (x1 - x2) / (v2 - v1) if v2 - v1 != 0 else 'NO'
    if v2 > v1:
        print('NO')
    elif v2 < v1 and t > 0 and str(t)[-1] == '0':
        print('YES')  
    else:
        print('NO')                    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    kangaroo(x1, v1, x2, v2)
    
 
 
