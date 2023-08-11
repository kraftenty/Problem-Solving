import sys;input=sys.stdin.readline
from collections import deque

#입력 파트
R,C=map(int,input().split()) #Row, Column
graph=[]
for _ in range(R):
    graph.append(list(input().rstrip()))

#자상하좌우 graphs
dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]
def bfs(yStart, xStart):
    sheepCnt=0
    wolfCnt=0
    q=deque()
    q.append((yStart,xStart))

    while q:
        y,x=q.popleft()
        for d in range(5):
            ny = y+dy[d]
            nx = x+dx[d]
            if 0<=ny<R and 0<=nx<C:
                if graph[ny][nx] != '#': #미방문 노드인 경우
                    if graph[ny][nx]=='o':
                        sheepCnt+=1
                    elif graph[ny][nx]=='v':
                        wolfCnt+=1
                    graph[ny][nx] = '#' #방문처리
                    q.append((ny,nx))

    if wolfCnt>=sheepCnt:
        return 0,wolfCnt
    else:
        return sheepCnt,0


survivedSheep=0
survivedWolf=0
for y in range(R):
    for x in range(C):
        if graph[y][x]!='#': #방문안했으면
            tmpSurvivedSheep, tmpSurvivedWolf=bfs(y,x)
            survivedSheep+=tmpSurvivedSheep
            survivedWolf+=tmpSurvivedWolf

print(f'{survivedSheep} {survivedWolf}')