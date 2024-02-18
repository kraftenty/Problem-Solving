import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append([int(e) for e in input().rstrip()])

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 지금까지의 거리를 내포한 방문표시


def bfs():
    dq = deque()
    dq.append((0, 0, 0))  # y, x, wasBreak(벽을 지금까지 한번이라도 부쉈는가? 0 or 1)
    visited[0][0][0], visited[0][0][1] = 1, 1
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

    while dq:
        y, x, wasBreak = dq.popleft()

        # 도착했을 때
        if y == N - 1 and x == M - 1:
            return visited[y][x][wasBreak]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 새로운 칸이 범위를 안벗어나고, 미방문지역일 때
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx][wasBreak] == 0:
                # 이동 가능하면(벽이 없음)
                if board[ny][nx] == 0:
                    visited[ny][nx][wasBreak] = visited[y][x][wasBreak] + 1
                    dq.append((ny, nx, wasBreak))
                # 이동 불가능 하지만(벽이 있음), 벽을 아직 하나도 안부쉈으면
                elif board[ny][nx] == 1 and wasBreak == 0:
                    visited[ny][nx][wasBreak + 1] = visited[y][x][wasBreak] + 1
                    dq.append((ny, nx, wasBreak + 1))

    # 탐색 실패
    return -1


print(bfs())