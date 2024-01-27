import sys

input = sys.stdin.readline

N = int(input())
# 2 5 7 1 3 4 8 6 9 3
li = list(map(int, input().split()))
cache = [0 for _ in range(N)]
cache.append(0)  # cache[-1]=0을 위해

for i in range(N):
    for j in range(i, -1, -1):
        cache[i] = max(cache[i], abs(li[i]-li[j]) + cache[j-1])

print(cache[N-1])