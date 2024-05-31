func boj7785() {
    let count = Int(readLine()!)!
    var dict: [String: Bool] = [:]
    
    for i in 0...count-1 {
        let log = readLine()!.split(separator: " ").map { String($0) }
        if log[1] == "enter" {
            dict[log[0]] = true
        } else {
            dict[log[0]] = nil
        }
    }

    for name in dict.keys.sorted(by: > ) {
        print(name)
    }
    
}

boj7785()
