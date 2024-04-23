N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = [0 for _ in range(M)]
check = [0] * N

def perm(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            result[depth] = arr[i]
            perm(depth + 1)
            check[i] = 0

perm(0)