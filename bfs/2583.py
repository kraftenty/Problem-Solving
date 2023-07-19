import sys;

input = sys.stdin.readline
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(ystart, xstart):
    cnt = 1
    q = deque()
    q.append((ystart, xstart))
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if (0 > ny or ny >= M) or (0 > nx or nx >= N) or graph[ny][nx] != 0:
                continue
            graph[ny][nx] = 1
            q.append((ny, nx))
            cnt += 1
    return cnt


M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i, j))

print(len(res))
res.sort()
for val in res:
    print(val, end=' ')
