import sys

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())


def bfs(initLoc, endLoc):
    q = deque()
    q.append((initLoc, 0))
    MAX_LEN = 100001
    visited = [False]*MAX_LEN
    visited[initLoc]=True
    while q:
        loc, hop = q.popleft()

        if loc == endLoc:
            return hop

        if 0<=(loc+1)<MAX_LEN and not visited[loc+1]:
            visited[loc+1]=True
            q.append((loc + 1, hop + 1))
        if 0<=(loc-1)<MAX_LEN and not visited[loc-1]:
            visited[loc-1]=True
            q.append((loc - 1, hop + 1))
        if 0<=(loc*2)<MAX_LEN and not visited[loc*2]:
            visited[loc*2]=True
            q.append((loc * 2, hop + 1))


result = bfs(N, K)
print(result)
