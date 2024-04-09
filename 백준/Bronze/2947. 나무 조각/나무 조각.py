arr = list(map(int, input().split()))

for _ in range(len(arr)):
    for i in range(len(arr)):
        for j in range(i+1,i+2):
            if j > len(arr) - 1:
                continue
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(*arr)
