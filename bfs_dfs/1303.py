import sys
from collections import deque

input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
def bfs(ystart, xstart):
    count = 1
    teamChar = graph[ystart][xstart]
    graph[ystart][xstart] = 'V'
    q = deque()
    q.append((ystart, xstart))
    while q:
        ny, nx = q.popleft()
        for dy, dx in direction:
            ty = ny + dy
            tx = nx + dx
            if 0 <= ty < R and 0 <= tx < C and graph[ty][tx] == teamChar:
                count += 1
                graph[ty][tx]='V'
                q.append((ty,tx))

    return teamChar, count


C, R = map(int, input().split())
graph = list()
for _ in range(R):
    line = list(input().rstrip())
    graph.append(line)

whitePower = 0
bluePower = 0
for y in range(R):
    for x in range(C):
        if graph[y][x] != 'V':
            teamChar, count = bfs(y, x)
            if teamChar=='W':
                whitePower+= count**2
            else:
                bluePower+= count**2

print(f'{whitePower} {bluePower}')
