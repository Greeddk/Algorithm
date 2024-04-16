func sol9012() {
    let total = Int(readLine()!)!
    
    var answer: [Bool] = []
    
    for _ in 1...total {
        let line = readLine()!
        answer.append(check(line))
    }
    
    for i in 0..<total {
        let answerString = answer[i] ? "YES" : "NO"
        print(answerString)
    }
    
    func check(_ line: String) -> Bool {
        var count = 0
        for element in line {
            if element == "(" {
                count += 1
            } else {
                if count <= 0 {
                    return false
                } else {
                    count -= 1
                }
            }
        }
        return count == 0 ? true : false
    }
}

sol9012()