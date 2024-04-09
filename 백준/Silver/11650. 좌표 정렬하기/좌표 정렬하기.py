cases = int(input())
coor = [list(map(int, input().split())) for _ in range(cases)]

coor.sort()
for i in coor:
    print(i[0], end=" ")
    print(i[1])