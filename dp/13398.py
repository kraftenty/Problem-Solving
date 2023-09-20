import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))

L = [0] * n
L[0] = a[0]
result = L[0]
for i in range(1, n):
    L[i] = max(a[i], L[i - 1] + a[i])
    result = max(result, L[i])

R = [0] * n
R[n - 1] = a[n - 1]
for i in range(n - 2, -1, -1):
    R[i] = max(a[i], R[i + 1] + a[i])

for i in range(1, n - 1):
    result = max(result, L[i - 1] + R[i + 1])

print(result)
