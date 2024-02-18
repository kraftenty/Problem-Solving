import sys

input = sys.stdin.readline

N = int(input())  # 구매하려고 하는 카드 개수
P = list(map(int, input().split()))
P.insert(0, 0)

dp = [0] * (N + 1)
for i in range(1, N + 1):  # 카드를 i 개 구매
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j])

print(dp[N])
# [0, 1, 5, 6, 7]
# 카드 1개들은 팩 1원
# 카드 2개들은 팩 5원
# 카드 3개들은 팩 6원
# 카드 4개들은 팩 7원
