import sys

input = sys.stdin.readline

N = int(input())
D = [[0] * 2 for _ in range(N + 1)]
# D[l][0] : 길이가 l이고 0으로 끝나는 이친수 의 개수
# D[l][1] : 길이가 l이고 1으로 끝나는 이친수 의 개수
D[1][0] = 0
D[1][1] = 1

for i in range(2, N + 1):
    D[i][0] = D[i - 1][1] + D[i - 1][0]
    D[i][1] = D[i - 1][0]

print(D[N][0] + D[N][1])
