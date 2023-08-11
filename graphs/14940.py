import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    line=list(map(int,input().split()))
    graph.append(line)

#방문 체크
visited=[[False]*m for _ in range(n)]
#결과(시작점 <-> 목표점 거리)
result=[[0]*m for _ in range(n)]

#시작지점 좌표 찾기
startY=0
startX=0
for y in range(n):
    for x in range(m):
        if graph[y][x]==2:
            startY=y
            startX=x
        elif graph[y][x]==0:
            visited[y][x]=True

#bfs시행. 격자 상하좌우
dir=[(1,0),(-1,0),(0,-1),(0,1)]
def bfs(startY, startX):
    visited[startY][startX]=True
    q=deque()
    q.append((startY, startX))

    while q:
        y,x = q.popleft()
        for dy, dx in dir:
            ty = y + dy
            tx = x + dx
            if 0<=ty<n and 0<=tx<m and not visited[ty][tx]:
                if graph[ty][tx]!=0:
                    result[ty][tx] = result[y][x] + 1
                    visited[ty][tx] = True
                    q.append((ty, tx))
            

bfs(startY, startX)

# print('[visited]')
# for y in range(n):
#     for x in range(m):
#         if visited[y][x]:
#             print('v', end = ' ')
#         else:
#             print('x', end = ' ')
#     print()

# print('[result]')
for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            print(-1, end = ' ')
        else:
            print(result[y][x], end = ' ')
    print()

