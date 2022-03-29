def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    count_max = 0
    count_min = 0
    for i in scores[1:]:
        if i > max_score:
            max_score = i
            count_max += 1
        elif i < min_score:
            min_score = i
            count_min += 1
        else:
            pass        
    return f'{count_max} {count_min}'    
        
if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    
    print(result)
 
 
