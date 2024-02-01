import sys

input = sys.stdin.readline

INF = 2**31 -1

def print_dp_table():
    for i in range(N):
        for j in range(N):
            print(dp[i][j], end=' ')
        print()


N = int(input())
m = []
for _ in range(N):
    m.append(tuple(map(int, input().split())))

dp = [[INF] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        dist = j-i
        for k in range(dist):
            dp[i][j] = min(
                dp[i][j],
                dp[i][i+k] + dp[i+k+1][j] + (m[i][0] * m[i+k][1] * m[j][1])
            )

print(dp[0][N-1])