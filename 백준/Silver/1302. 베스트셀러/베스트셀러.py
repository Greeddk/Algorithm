numberOfSoldBook = int(input())
bookSellingList = {}
for _ in range(numberOfSoldBook):
    bookName = input()
    bookSellingList[bookName] = bookSellingList.get(bookName, 0) + 1

bookName = []
for name in bookSellingList.keys():
    bookName.append(name)
bookName.sort()
maxNum = 0
answer = ""
for name in bookName:
    if maxNum < bookSellingList[name]:
        maxNum = bookSellingList[name]
        answer = name
print(answer)