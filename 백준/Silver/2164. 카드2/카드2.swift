struct QueuePointer<T> {
  private var elements: [T] = []
  private var front = 0

  var isEmpty: Bool {
    elements.count < front + 1
  }

  var count: Int {
    elements.count - front
  }

  func peek() -> T? {
    front < elements.count ? elements[front] : nil
  }

  mutating func enqueue(with element: T) {
    elements.append(element)
  }

  @discardableResult
  mutating func dequeue() -> T? {
    if !isEmpty {
      defer { front += 1 }
      return elements[front]
    } else {
      return nil
    }
  }
}

func sol2164() {
    let cards = Int(readLine()!)!
    var list = QueuePointer<Int>()
    let isDiscard = [true, false]
    var count = 0
    
    for i in 1...cards {
        list.enqueue(with: i)
    }
    
    while list.count != 1 {
        if isDiscard[count % 2] {
            list.dequeue()
        } else {
            list.enqueue(with: list.dequeue()!)
        }
        count += 1
    }
    
    print(list.dequeue()!)
    
}

sol2164()