import sys
input = sys.stdin.readline

def dfs(now, cost, depth):
    global ans

    if depth == N:                          # 기저사례
        if cost_matrix[now][0]:             # 마지막 도착지에서 출발지(0)로 가는 길이 있다면
            cost += cost_matrix[now][0]     # 해당 비용을 더하고
            ans = min(ans, cost)            # 정답 갱신
            return
        else:                               # 마지막 도착지에서 출발지(0)로 가는 길이 없으면 그냥 리턴
            return
    
    if cost > ans:                          # 백트래킹
        return
    
    for after in range(N):
        if visited[after] or not cost_matrix[now][after]:
            continue
        
        visited[after] = 1
        dfs(after, cost+cost_matrix[now][after], depth+1)
        visited[after] = 0

N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 987654321

visited[0] = 1
dfs(0, 0, 1)

print(ans)