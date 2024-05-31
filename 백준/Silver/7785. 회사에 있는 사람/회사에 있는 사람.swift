func boj7785() {
    let count = Int(readLine()!)!
    var list: [String: Bool] = [:]
    
    for i in 0...count-1 {
        let log = readLine()!.split(separator: " ")
        if log[1] == "enter" {
            list[String(log[0])] = true
        } else {
            list[String(log[0])] = false
        }
    }
    
    var inCompanyList: [String] = []
    for item in list {
        if item.value == true {
            inCompanyList.append(item.key)
        }
    }
    
    inCompanyList.sort(by: >)
    
    for name in inCompanyList {
        print(name)
    }
    
}

boj7785()