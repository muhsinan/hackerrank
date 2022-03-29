def timeConversion(s):
    if 'PM' in s and s[0] == '0':
        s = s.replace('PM', '')
        s = s.replace(s[0:2], str(int(s[1]) + 12))
    elif 'PM' in s and s[0] == '1' and s[0:2] != '12':
        s = s.replace('PM', '')
        s = s.replace(s[0:2], str(int(s[0:2]) + 12))
    elif 'AM' in s and s[0:2] == '12':
        s = s.replace('AM', '')
        s = s.replace(s[0:2], '00')
    elif 'PM' in s and s[0:2] == '12':
        s = s.replace('PM', '')
    else:
        s = s.replace('AM', '')
    return s            
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    
    print(result)
 
