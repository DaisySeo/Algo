def solution(dartResult):
    temp = []
    mark = 0
    n = 0
    for dart in dartResult:
        if(dart.isalpha()):
            temp.append(dartResult[mark:n+1])
            mark = n + 1
        if n+1 == len(dartResult):
            if dart == '#' or dart == '*':
                temp.append(dart)
        n = n + 1

    #print(temp)
    
    arr = []
    cnt = 0
    for item in temp:
        if item[0] == '#':
            arr[cnt-1] = arr[cnt-1] * (-1)
            item = item.replace('#', '')
            
        elif item[0] == '*':
            arr[cnt-1] = arr[cnt-1] * 2
            if cnt == 2 or cnt == 3:
                arr[cnt-2] = arr[cnt-2] * 2
            item = item.replace('*', '')
            
        if cnt == 3:
            break
        
        if item[-1] == 'S':
            arr.append(int(item[:-1]) ** 1)
        elif item[-1] == 'D':
            arr.append(int(item[:-1]) ** 2)
        elif item[-1] == 'T':
            arr.append(int(item[:-1]) ** 3)
            
        cnt = cnt + 1
        
    #print(arr)
    
    answer = 0
    for var in arr:
        answer = answer + var
    #print answer
    return answer
