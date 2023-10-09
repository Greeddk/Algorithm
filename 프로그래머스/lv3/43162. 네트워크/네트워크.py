from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문 여부를 저장하는 리스트를 False로 초기화합니다.
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = True  # 시작 노드를 방문했다고 표시합니다.
        
        while queue:
            cur_node = queue.popleft()
            for i in range(n):
                if computers[cur_node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 노드인 경우에만 BFS를 수행합니다.
            bfs(i)
            answer += 1

    return answer

