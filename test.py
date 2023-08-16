import sys

input = sys.stdin.readline
a = [1, 2, 3, 4, 5]
N = 5
# 1 2 3 4 5
# 5 1 2 3 4
# 4 5 1 2 3

shiftValue=2

for i in range(N-shiftValue, N):
    print(a[i], end=' ')

for i in range(0, N-shiftValue):
    print(a[i], end=' ')

