import sys

input = sys.stdin.readline

N = int(input())
l = list()
for _ in range(N):
    l.append(list(map(int, input().split(' '))))

# DP
# l[i][0]: R색상
# l[i][1]: G색상
# l[i][2]: B색상
for i in range(1, N):
    l[i][0] += min(l[i - 1][1], l[i - 1][2])
    l[i][1] += min(l[i - 1][0], l[i - 1][2])
    l[i][2] += min(l[i - 1][0], l[i - 1][1])

res = min(l[N - 1][0], l[N - 1][1], l[N - 1][2])
print(res)
