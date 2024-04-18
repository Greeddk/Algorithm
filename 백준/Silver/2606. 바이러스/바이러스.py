from collections import deque

V = int(input())
E = int(input())

adj = [[] for _ in range(V + 1)]
visited = set()
queue = deque([1])

for i in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

while len(queue) != 0:
    current = queue.popleft()
    visited.add(current)

    for i in adj[current]:
        if i not in visited:
            queue.append(i)

print(len(visited) - 1)