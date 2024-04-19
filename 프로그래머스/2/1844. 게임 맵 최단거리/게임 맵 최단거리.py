# from collections import deque

# def solution(maps):
#     answer = -1
#     row = len(maps[0])
#     col = len(maps)
    
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     queue = deque([(0,0)])

#     while queue:
#         cur_y, cur_x = queue.popleft()
#         for i in range(4):
#             next_x = cur_x + dx[i]
#             next_y = cur_y + dy[i]
#             if next_x in range(row) and next_y in range(col):
#                 if maps[next_y][next_x] == 1:
#                     queue.append((next_y,next_x))
#                     maps[next_y][next_x] = maps[cur_y][cur_x] + 1
#                 if next_x == row - 1 and next_y == col - 1:
#                     return maps[next_y][next_x]

#     return answer

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
    
def solution(maps):
    row, col = len(maps), len(maps[0])
    answer = -1
    queue = deque([(1,0,0)])
    visited = set([(0,0)])

    while queue:
        cnt, r, c = queue.popleft()
        if r == row-1 and c == col-1:
            answer = cnt
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and maps[nr][nc] != 0:
                queue.append((cnt+1, nr, nc)) 
                visited.add((nr, nc))
    return answer