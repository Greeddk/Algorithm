n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

def sol(n, arr, budget):
    start = 0
    end = max(arr)
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for i in arr:
            total += min(i, mid)
        
        if total <= budget:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return answer

print(sol(n, arr, budget))