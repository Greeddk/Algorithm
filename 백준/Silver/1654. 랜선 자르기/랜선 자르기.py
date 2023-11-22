k,n = map(int, input().split())
arr = []

for _ in range(k):
    arr.append(int(input()))

arr.sort()

def sol(n,arr):
    start = 1
    end = arr[-1]
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for i in arr:
            total += (i // mid)
#       total 값이 만들어야하는 수 보다 적으면 end를 줄여서 더 많이 자를 수 있게 해줘야함
        if total < n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer

print(sol(n,arr))
