from itertools import combinations

height = []
for i in range(9):
    height.append(int(input()))
    

arr = list(combinations(height, 7))
result = []
for i in arr:
    sumValue = 0
    for j in i:
        sumValue += j
    if sumValue == 100:
        for j in i:
            result.append(j)
        break

result.sort()
for i in result:
    print(i)