def countingValleys(steps, path):
    altitude = 0
    sea = 0
    for i in path:
        if i == 'U':
            altitude += 1
            if altitude == 0:
                sea +=1
        else:
            altitude -= 1
    return sea        
if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    
    print(result)
 
 
