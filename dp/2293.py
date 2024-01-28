import sys

input = sys.stdin.readline

# 3, 10
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))


cache = [0] * (k + 1)
cache[0] = 1

for i in range(n):
    for j in range(1, k+1):
        if j >= coins[i]:
            cache[j] += cache[j-coins[i]]

print(cache[k])
