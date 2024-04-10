n,m = map(int, input().split())
arr = list(map(int,input().split()))
section = [list(map(int,input().split())) for _ in range(m)]
sigma = [0] * (len(arr)+1)

for i in range(1, len(arr)+1):
    sigma[i] = sigma[i-1] + arr[i-1]

for i in range(len(section)):
    answer = sigma[section[i][1]] - sigma[section[i][0]-1]
    print(answer)