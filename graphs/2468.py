import sys

input = sys.stdin.readline
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(ystart, xstart):
    q = deque()
    q.append((ystart, xstart))
    while q:
        ty, tx = q.popleft()
        for d in range(4):
            ny = ty + dy[d]
            nx = tx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] > height and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

    return 1


maxHeight = 0

N = int(input())
graph = []
for _ in range(N):
    line = list(map(int, input().split()))
    maxHeight = max(line)
    graph.append(line)

maxSafeAreaCnt = 1
for height in range(1, maxHeight):
    visited = [[False] * N for _ in range(N)]
    tmpSafeAreaCnt = 0
    for y in range(N):
        for x in range(N):
            if graph[y][x] > height and not visited[y][x]:
                visited[y][x] = True
                tmpSafeAreaCnt += bfs(y, x)
    maxSafeAreaCnt = max(maxSafeAreaCnt, tmpSafeAreaCnt)

print(maxSafeAreaCnt)
