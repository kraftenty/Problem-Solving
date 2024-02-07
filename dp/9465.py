import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    b = [list(map(int, input().split(' '))) for _ in range(2)]

    # b
    # 50 10 100 20 40
    # 30 50 70  10 60

    dp = [[0 for _ in range(n+1)] for _ in range(2)]  # 의미: 전 col까지의 Max 누적 값
    # 초기 첫 col 세팅
    dp[0][1] = b[0][0]
    dp[1][1] = b[1][0]
    # dp
    # 0 30 0 0 0
    # 0 50 0 0 0
    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + b[0][i-1]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + b[1][i-1]

    print(max(dp[0][n], dp[1][n]))
