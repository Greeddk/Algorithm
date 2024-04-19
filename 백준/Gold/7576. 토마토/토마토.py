from collections import deque

col, row = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(row)]

queue = deque()
answer = -1

for i in range(row):
    for j in range(col):
        if arr[i][j] == 1:
            queue.append((i,j))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and arr[nr][nc] == 0:
            arr[nr][nc] = arr[r][c] + 1
            queue.append((nr, nc))

ans = 0
for index in arr:
    if 0 in index:
        ans = 0
        break

    ans = max(ans, max(index))
    
print(ans - 1)