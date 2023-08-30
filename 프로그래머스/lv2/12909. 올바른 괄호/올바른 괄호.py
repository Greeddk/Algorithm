def solution(s):
    answer = True
    stack = []
    arr = list(s)
    cnt = 0
    for i in arr:
        if cnt < 0:
            break
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -=  1
            
    
    
    if arr[0] == '(' and arr[-1] == ')' and cnt == 0:
        answer = True
    else:
        answer = False
        
    return answer