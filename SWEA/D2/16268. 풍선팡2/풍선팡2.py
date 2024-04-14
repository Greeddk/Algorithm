def boom(arr):
    dr = [1, 0 , -1, 0]
    dc = [0, 1, 0, -1]
    answer = 0
    for r in range(row):
        for c in range(column):
            value = arr[r][c]
            for direction in range(4):
                nr, nc = r + dr[direction], c + dc[direction]

                if 0 <= nr < row and 0 <= nc < column:
                    value += arr[nr][nc]

            answer = max(answer, value)
    return answer


for tc in range(1, int(input()) + 1):
    row, column = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]
    dr = [1, 0 , -1, 0]
    dc = [0, 1, 0, -1]

    print(f'#{tc} {boom(arr)}')
    