def solution(k, dungeons):
    answer = 0

    visited = [0] * len(dungeons)

    def dfs(depth, k):
        nonlocal answer
        answer = max(answer, depth)

        for i in range(len(dungeons)):
            if visited[i] == 0 and k >= dungeons[i][0]:
                visited[i] = 1
                dfs(depth + 1, k - dungeons[i][1])
                visited[i] = 0

    dfs(0, k)
    return answer