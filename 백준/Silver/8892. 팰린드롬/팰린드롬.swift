func check_palindrome(one: String, two: String) -> Bool {
    
    let target = one + two
    return target == String(target.reversed())
}

func generatePalindromes(list: [String]) {
    for i in 0..<list.count {
        for j in 0..<list.count {
            if i == j { continue }
            let palindrome = check_palindrome(one: list[i], two: list[j])
            if palindrome {
                print("\(list[i])\(list[j])")
                return
            }
        }
    }
    print("0")
}

func boj8892() {
    let cases = Int(readLine()!)!
    for _ in 0...cases-1 {
        let inputNum = Int(readLine()!)!
        var list: [String] = []
        
        for _ in 0...inputNum-1 {
            let word = String(readLine()!)
            list.append(word)
        }

        generatePalindromes(list: list)
    }
}

boj8892()