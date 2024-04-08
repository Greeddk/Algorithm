arr = []
for i in range(10):
    arr.append(int(input()))
value = {}
for num in arr:
    value[num%42] = value.get(num%42,0) 

print(len(value))