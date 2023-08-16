import sys
input=sys.stdin.readline

N=int(input())

D = [[0 for _ in range(10)] for _ in range(N+1)]
for i in range(1, 10):
    D[1][i]=1

for length in range(2, N+1):
    D[length][0] = D[length-1][1]
    D[length][9] = D[length-1][8]
    for level in range(1, 9):
        D[length][level] = D[length-1][level-1] + D[length-1][level+1]

sum = 0
for i in range(0, 10):
    sum += D[N][i]
print(sum % 1000000000)