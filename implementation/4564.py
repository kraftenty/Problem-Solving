import sys

input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == '0':
        break

    print(S, end=' ')
    while len(S) > 1:
        tmp = 1
        for n in S:
            tmp *= int(n)
        S = str(tmp)
        print(S, end=' ')
