let input = Int(readLine()!)!

var array: [[String]] = []
var touchArray: [[String]] = []
var answer: [[String]] = .init(repeating: .init(repeating: ".", count: input), count: input)

for _ in 0..<input {
    let line = readLine()!.map { String($0) }
    array.append(line)
}

for _ in 0..<input {
    let line = readLine()!.map { String($0) }
    touchArray.append(line)
}

func checkAround(col: Int, row: Int) -> Int {
    let dc = [1,1,1,0,0,-1,-1,-1]
    let dr = [-1,0,1,-1,1,-1,0,1]
    var sum = 0

    for d in 0..<8 {
        let nc = col + dc[d]
        let nr = row + dr[d]
        
        if 0 <= nc && nc < input && 0 <= nr && nr < input {
            if array[nc][nr] == "*" {
                sum += 1
            }
        }
    }
    
    return sum
}

var mineClicked = false

for i in 0..<input {
    for j in 0..<input {
        if touchArray[i][j] == "x" {
            if array[i][j] == "*" {
                mineClicked = true
            } else {
                answer[i][j] = String(checkAround(col: i, row: j))
            }
        }
    }
}

if mineClicked {
    for i in 0..<input {
        for j in 0..<input {
            if array[i][j] == "*" {
                answer[i][j] = "*"
            }
        }
    }
}

for line in answer {
    print(line.joined())
}