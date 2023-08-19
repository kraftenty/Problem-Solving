import sys

input = sys.stdin.readline

P = list(map(int, input().split(' ')))
N = P[0]
del P[0]

for i in range(4):
    P[i] = P[i] / 100

visited = [[False] * (N * 2 + 1) for _ in range(N * 2 + 1)]

#          v
# 동 -> 동, 서, 남, 북
#      v      
# 서 -> 동, 서, 남, 북
#                 v
# 남 -> 동, 서, 남, 북
#             v
# 북 -> 동, 서, 남, 북

# 전체=16 (4**N)
# 단순하지 않음(visited 겹침)=4
# 단순함=12
# 단순할 확률 = 12/16 * 100 = 75 (%)


dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)

answer = 0


def dfs(y, x, cnt, res):
    global answer

    if cnt == N:
        answer += res
        return

    visited[y][x] = True

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]

        if not visited[ty][tx]:
            dfs(ty, tx, cnt + 1, res * P[i])

    visited[y][x] = False


dfs(N, N, 0, 1.0)
print(answer)
