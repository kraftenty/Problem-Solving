import sys
from collections import deque

input = sys.stdin.readline

YMAX, XMAX = map(int, input().split(' '))
graph = list()
for line in range(YMAX):
    graph.append(list(input().rstrip()))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(startY, startX):
    q = deque()
    q.append((startY, startX, 0))
    visited = [[False] * XMAX for _ in range(YMAX)]  # -1 : 미방문 노드
    visited[startY][startX] = True

    maxHop = -1
    while q:
        y, x, hop = q.popleft()
        if hop > maxHop:
            maxHop = hop
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < YMAX and 0 <= tx < XMAX and not visited[ty][tx] and graph[ty][tx] == 'L':
                visited[ty][tx] = True
                q.append((ty, tx, hop + 1))
    return maxHop


result = -1
for ly in range(YMAX):
    for lx in range(XMAX):
        if graph[ly][lx] == 'L':
            result = max(result, bfs(ly, lx))

print(result)
