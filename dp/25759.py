# 반복문으로 풀기
# N = int(input())
# A = list(map(int, input().split()))

# dp = [-1] * 101
# dp[A[0]] = 0


# for beauty in A:
#     for k in range(1, 101):
#         if dp[k] >= 0:
#             dp[beauty] = max(dp[beauty], dp[k] + (beauty-k)**2)

# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))
table = [[-1 for _ in range(101)] for _ in range(n)]

def DP(idx, before):
    if idx == n:
        return 0

    if table[idx][before] != -1:
        return table[idx][before]

    table[idx][before] = max(DP(idx+1, arr[idx]) + (arr[idx] - before)**2 , DP(idx+1, before))
    return table[idx][before]

print(DP(0, arr[0]))