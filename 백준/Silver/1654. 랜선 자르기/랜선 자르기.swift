let input = readLine()!.split(separator: " ").map { Int($0)! }
let k = input[0]
let n = input[1]

var list: [Int] = []

for _ in 0..<k {
    list.append(Int(readLine()!)!)
}

var start = 1
var end = list.max()!
var maxLeng = 0

while start <= end {
    var stringCount = 0
    var mid = (start + end) / 2
    
    for num in list {
        stringCount += num / mid
    }
    
    if stringCount < n {
        end = mid - 1
    } else {
        start = mid + 1
        maxLeng = max(maxLeng, mid)
    }

}
print(maxLeng)
