V = int(input())
E = int(input())
# 인접리스트 DFS
adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = set()
def dfs(cur):
    visited.add(cur)

    for next in adj[cur]:
        if next not in visited:
            dfs(next)

dfs(1)

print(len(visited)-1)