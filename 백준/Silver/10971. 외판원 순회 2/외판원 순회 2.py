T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

#세팅
visited = [0] * T
answer = 987654321

def dfs(depth, cost, cur):
    global answer

    # 방문
    if depth == T:
        if arr[cur][0]:
            cost += arr[cur][0]
            answer = min(answer, cost)
            return
        else:
            return
        
    # 백트래킹
    if cost > answer:
        return

    # 탐색
    for i in range(T):
        if visited[i] or not arr[cur][i]:
            continue
        

        visited[i] = 1
        dfs(depth+1, cost + arr[cur][i], i)
        visited[i] = 0
        

            
visited[0] = 1
dfs(1, 0, 0)
print(answer)