num_people = int(input())
arr = list(map(int, input().split()))

def min_time():
    arr.sort()
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]

    return sum(arr)

print(min_time())
