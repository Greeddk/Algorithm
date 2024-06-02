let nm = readLine()!.split(separator: " ").map{Int(String($0))!}
let n = nm[0]
let m = nm[1]
let arr = readLine()!.split(separator: " ").map{Int(String($0))!}

var start = 0
var end = arr.max()!

while start <= end {
    var sum = 0
    let mid = (start + end) / 2
    
    for i in arr{
        if i - mid < 0{continue}
        sum += (i - mid)
    }
    
    if sum < m {
        end = mid - 1
    } else {
        start = mid + 1
    }
}
print(start - 1)