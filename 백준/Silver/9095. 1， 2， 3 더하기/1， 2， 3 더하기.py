n = int(input())

memo = {1: 1, 2: 2, 3: 4}

def solution(targetNum):
    for i in range(4, targetNum + 1):
        if i not in memo:
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return print(memo[targetNum])

for i in range(n):
    targetNum = int(input())
    solution(targetNum)