n,k = map(int, input().split())
arr = list(map(int, input().split()))

preSum = [0]*(n+1)

for i in range(1,n+1):
    preSum[i] = preSum[i-1] + arr[i-1]

answer = []
for i in range(k,n+1):
    value = preSum[i] - preSum[i-k]
    answer.append(value)
print(max(answer))

