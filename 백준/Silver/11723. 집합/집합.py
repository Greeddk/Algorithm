import sys
input = sys.stdin.readline

S = 0  # 집합을 나타내는 비트마스크 변수 S를 초기화합니다.

# 입력을 받고 연산을 수행합니다.
for _ in range(int(input())):
    commands = input().rstrip().split()  # 명령을 읽고 공백을 기준으로 나눕니다.

    if len(commands) == 1:  # 명령이 한 단어로만 이루어져 있다면
        if commands[0] == 'all':  # 'all'이면
            S = (1 << 21) - 1  # 모든 비트를 1로 설정하여 집합을 초기화합니다.
        elif commands[0] == 'empty':  # 'empty'이면
            S = 0  # 모든 비트를 0으로 설정하여 공집합으로 만듭니다.
    else:  # 명령이 두 단어로 이루어져 있다면
        command, num = commands[0], int(commands[1])  # 명령과 숫자를 추출합니다.
        num -= 1  # 문제에서 주어진 숫자는 1부터 시작하지만, 인덱스는 0부터 시작하므로 1을 뺍니다.
        if command == 'add':  # 'add' 명령이면
            S |= (1 << num)  # 해당 위치의 비트를 1로 설정하여 원소를 추가합니다.
        elif command == 'remove':  # 'remove' 명령이면
            S &= ~(1 << num)  # 해당 위치의 비트를 0으로 설정하여 원소를 제거합니다.
        elif command == 'check':  # 'check' 명령이면
            if S & (1 << num):  # 해당 위치의 비트가 1인지 확인합니다.
                print(1)  # 1이면 집합에 있는 것이므로 1을 출력합니다.
            else:
                print(0)  # 0이면 집합에 없는 것이므로 0을 출력합니다.
        elif command == 'toggle':  # 'toggle' 명령이면
            S ^= (1 << num)  # 해당 위치의 비트를 반전시켜서 추가하거나 제거합니다.
