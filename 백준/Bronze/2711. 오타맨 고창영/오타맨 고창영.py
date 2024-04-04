T = int(input())

for tc in range(T):
    idx, word = list(map(str,input().split(" ")))
    idx = int(idx)
    answer = word[:idx-1] + word[idx:]
    print(answer)
    