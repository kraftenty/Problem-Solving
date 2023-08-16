import sys

input = sys.stdin.readline

N, Q = map(int, input().split(' '))

a = list(map(int, input().split(' ')))

shiftValue = 0
for _ in range(Q):
    queryList = list(map(int, input().rstrip().split(' ')))
    if queryList[0] == 1:
        a[(queryList[1] + shiftValue - 1) % N] += queryList[2]
    elif queryList[0] == 2:  # 오른쪽으로 시프트
        shiftValue -= queryList[1]
    elif queryList[0] == 3:  # 왼쪽으로 시프트
        shiftValue += queryList[1]

for i in range(shiftValue, shiftValue + N):
    print(a[i % N], end=' ')


