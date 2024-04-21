func boj7576() {
    // 배열 크기 입력
    let size = readLine()!.split(separator: " ").map { Int($0)! }
    let col = size[0]
    let row = size[1]
    
    // 배열 세팅
    var arr: [[Int]] = []
    var queue: [(Int, Int)] = []
    var front: Int = 0
    
    for _ in 0..<row {
        let rowList = readLine()!.split(separator: " ").map { Int($0)! }
        arr.append(rowList)
    }

    // 시작점 찾기
    for i in 0..<row {
        for j in 0..<col {
            if arr[i][j] == 1 {
                queue.append((i,j))
            }
        }
    }

    // 델타 탐색 세팅
    let dr = [0, 1, 0, -1]
    let dc = [1, 0, -1, 0]
    
    while queue.count != front {
        let current = queue[front]
        let r = current.0
        let c = current.1

        for direction in 0..<4 {
            let nr = r + dr[direction]
            let nc = c + dc[direction]
            
            if 0 <= nr && nr < row && 0 <= nc && nc < col && arr[nr][nc] == 0 {
                queue.append((nr, nc))
                arr[nr][nc] = arr[r][c] + 1
            }
        }
        front += 1
    }
    
    var answer = 0
    
    for line in arr {
        if line.contains(0) {
            answer = 0
            break
        }
        for value in line {
            answer = max(answer, value)
        }
    }
    
    print(answer - 1)
}

boj7576()