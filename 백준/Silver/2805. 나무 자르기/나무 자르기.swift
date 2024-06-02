func boj2805() {
    let input = readLine()!.split(separator: " ").compactMap{ Int($0)! }
    let treeNumber = input[0]
    let treeLeng = input[1]
    
    let list = readLine()!.split(separator: " ").compactMap{ Int($0)! }

    var left = 1
    var right = list.max()!
    
    while left <= right {
        var sum = 0
        let mid = (left + right) / 2
        
        for i in list {
            if i - mid < 0 { continue }
            sum += (i - mid)
        }
        
        if sum < treeLeng {
            right = mid - 1
        } else {
            left = mid + 1
        }
        
    }
    
    print(left - 1)
}

boj2805()