import sys
input = sys.stdin.readline

N = int(input())
Q = int(input())
qy, qx = 0, 0
graph = [[0]*N for _ in range(N)]
graph[0][0]=N**2
# y x
# 하 우 상 좌
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dirPtr = 0

ny, nx = 0, 0
for i in range(N**2 -1, 0, -1):
    ty, tx = ny + dir[dirPtr][0], nx + dir[dirPtr][1]
    if ty<0 or ty>=N  or tx<0 or tx>=N or graph[ty][tx]!=0:
        if dirPtr==3:
            dirPtr=0
        else:
            dirPtr+=1

    ny += dir[dirPtr][0]
    nx += dir[dirPtr][1]
    graph[ny][nx] = i

    if i == Q:
        qy = ny
        qx = nx


for y in range(N):
    for x in range(N):
        print(graph[y][x], end = ' ')
    print()

print(qy+1, qx+1)
