meeting = int(input())
arr = []

for _ in range(meeting):
    x,y = map(int, input().split())
    arr.append([x,y])

arr.sort(key=lambda x: (x[1], x[0]))
answer = []
end_time = 0
for i in range(meeting):
    if i == 0:
        answer.append(arr[i])
        end_time = arr[i][1]
        continue
    if arr[i][0] >= end_time:
        answer.append(arr[i])
        end_time = arr[i][1]

print(len(answer))