import sys
input=sys.stdin.readline

N=int(input())
graph=[]
for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

whiteCount=0
blueCount=0

def func(n, y, x):
    global whiteCount
    global blueCount

    firstColor = graph[y][x]
    for dy in range(y, y+n):
        for dx in range(x, x+n):
            if graph[dy][dx] != firstColor:
                #색이 하나라도 다르면 --> 재귀호출 하고 리턴
                halfN = n//2
                func(halfN, y, x)
                func(halfN, y, x+halfN)
                func(halfN, y+halfN, x)
                func(halfN, y+halfN, x+halfN)
                return
    
    #색이 모두 같으면
    if firstColor == 0:
        whiteCount+=1
    else:
        blueCount+=1


    
func(N, 0, 0)
print(f'{whiteCount}\n{blueCount}')