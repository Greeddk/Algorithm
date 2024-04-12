import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))
answer = 0
cnt = 0
r = 0
l = 0

while True:

    if cnt < m:
        if r < n: #r포인터가 전체 배열 개수보다 작으면
            cnt += arr[r]
            r += 1
        else: #r포인터가 전체 배열 개수랑 같을 경우 끝! -> 어차피 l포인터를 데리고 와도 빼기밖에 안하니까 더하는 건 의미가 없음
            break
    elif cnt > m:
        cnt -= arr[l]
        l += 1
    if cnt == m:
        answer += 1
        cnt -= arr[l]
        l += 1

print(answer)
