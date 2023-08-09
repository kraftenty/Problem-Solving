import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split())) # 2 4 -10 4 -9

sortedLi=sorted(list(set(li))) # -10 -9 2 4
sortedMap = {sortedLi[i] : i for i in range(len(sortedLi))}
for num in li:
    print(sortedMap[num], end=' ')