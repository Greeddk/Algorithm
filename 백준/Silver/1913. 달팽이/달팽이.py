N = int(input())
arr = [[0]*N for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
direction = 0

r = -1
c = 0
cnt = N*N
while cnt != 0:
    idx = direction % 4
    r = r - dr[idx]
    c = c - dc[idx]
    if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
        arr[r][c] = cnt
        cnt -= 1
    else:
        r = r + dr[idx]
        c = c + dc[idx]
        direction += 1

for i in arr:
    print(*i)

target = int(input())

for i in range(N):
    for j in range(N):
        if arr[i][j] == target:
            print(i+1, j+1)