import sys;input=sys.stdin.readline
from collections import deque

#입력 파트
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))


#상하좌우 dfs
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(ystart, xstart):
    count=1
    q=deque()
    q.append((ystart,xstart))
    graph[ystart][xstart]=0

    while q:
        y,x=q.popleft()
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if ny<0 or ny>=N or nx<0 or nx>=N: #경계 바깥 예외
                continue
            if graph[ny][nx]==1: #미방문 노드인 경우
                graph[ny][nx]=0 #방문처리
                q.append((ny,nx))
                count+=1

    return count




res=[]
for y in range(N):
    for x in range(N):
        if graph[y][x]==1: #방문안했으면
            cnt=bfs(y,x) #bfs해서
            res.append(cnt) #단지 내 집의수 append


#총 단지수 출력
print(len(res))
#각 단지내 집의 수를 오름차순으로 정렬하여 출력
res.sort()
for num in res:
    print(num)