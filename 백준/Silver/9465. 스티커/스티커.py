def sol(col, arr1, arr2):
    for i in range(2, col + 1):
        if i == 2:
            arr2[1], arr1[1] = arr1[0] + arr2[1], arr1[1] + arr2[0]
        else:
            arr1[i-1] = max(arr2[i-2], arr2[i-3]) + arr1[i-1]
            arr2[i-1] = max(arr1[i-2], arr1[i-3]) + arr2[i-1]
    
    print(max(max(arr1),max(arr2)))

n = int(input())

for _ in range(n):
    arr1 = []
    arr2 = []
    col = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    # 최댓값 출력 코드
    sol(col, arr1, arr2)