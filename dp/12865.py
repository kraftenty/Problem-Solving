import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # 물품의 수 N, 배낭의 max 용량 K
weights = [0] * (N + 1)
values = [0] * (N + 1)
for i in range(1, N + 1):
    weights[i], values[i] = map(int, input().split())  # Weight, Value

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# [
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, ?, ?, ?, ?, ?, ?, ?],
# [0, ?, ?, ?, ?, ?, ?, ?],
# [0, ?, ?, ?, ?, ?, ?, ?],
# [0, ?, ?, ?, ?, ?, ?, ?],
# ]

# # 물건을 아무것도 안담을 때
# for i in range(K+1):
#     dp[0][i] = 0
#
# # 배낭의 용량이 0일 때
# for i in range(N+1):
#     dp[i][0] = 0

for i in range(1, N + 1):
    for tmp_weight in range(1, K + 1):
        # i번째 물건의 weight가 tmp_weight보다 큰 경우(안들어가는 경우)
        if weights[i] > tmp_weight:
            dp[i][tmp_weight] = dp[i - 1][tmp_weight]
        # 들어가는 경우, i번째 물건을 담을지 말지 결정
        else:
            dp[i][tmp_weight] = max(dp[i - 1][tmp_weight], dp[i - 1][tmp_weight - weights[i]] + values[i])

# 결과 출력
print(dp[N][K])
