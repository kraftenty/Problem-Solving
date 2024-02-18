import sys

input = sys.stdin.readline

dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]


def w(a, b, c):
    # 메모이제이션 되어있는 값이면 바로 출력
    if (a>=0 and b>=0 and c>=0) and dp[a][b][c] != 0:
        return dp[a][b][c]

    # 제시된 조건
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


while True:
    A, B, C = map(int, input().split())
    if A == -1 and B == -1 and C == -1:
        break
    print(f'w({A}, {B}, {C}) = {w(A, B, C)}')
