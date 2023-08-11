import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    q = deque()
    q.append((startY, startX))
    while q:
        ny, nx = q.popleft()
        if ny == goalY and nx == goalX:
            return count[ny][nx] - 1
        for dy, dx in move:
            ty = ny + dy
            tx = nx + dx
            if 0 <= ty < l and 0 <= tx < l and count[ty][tx] == 0:
                count[ty][tx] = (count[ny][nx] + 1)
                q.append((ty, tx))


TC = int(input())
for _ in range(TC):
    l = int(input())  # 체스판 한 변의 길이
    startY, startX = map(int, input().split())  # now(현재 있는 칸)
    goalY, goalX = map(int, input().split())  # goal(이동하려고 하는 칸)

    count = [[0] * l for _ in range(l)]
    count[startY][startX] = 1
    print(bfs())
