import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))
answer = 0
cnt = 0
right = 0
left = 0

while True:

    if cnt < m:
        if right < n:
            cnt += arr[right]
            right += 1
        else:
            break
    elif cnt == m:
        answer += 1
        cnt -= arr[left]
        left += 1

    else:
        cnt -= arr[left]
        left += 1


print(answer)
