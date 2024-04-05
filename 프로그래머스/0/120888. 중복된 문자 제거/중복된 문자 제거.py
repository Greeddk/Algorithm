def solution(my_string):
    answer = ''
    tickets = set(my_string)

    for i in my_string:
        if i in tickets:
            answer += i
            tickets.remove(i)

    return answer