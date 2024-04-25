T = int(input())
answer = 0

check = [0] * T
leftCheck = [0] * (2 * T - 1)
rightCheck = [0] * (2 * T - 1)

def dfs(depth):
    global answer

    if depth == T:
        answer += 1
        return
    
    for i in range(T):
        if check[i] or leftCheck[depth + i] or rightCheck[depth - i]:
            continue

        check[i] = 1
        leftCheck[depth + i] = 1
        rightCheck[depth - i] = 1
        dfs(depth + 1)
        check[i] = 0
        leftCheck[depth + i] = 0
        rightCheck[depth - i] = 0

dfs(0)
print(answer)