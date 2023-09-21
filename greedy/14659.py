import sys
input=sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))

cnt = 0
maxCnt = 0
maxVal = 0
for i in range(N):
    if li[i]>maxVal:
        maxVal = li[i]
        cnt = 0
    else:
        cnt += 1
        maxCnt = max(cnt, maxCnt)

print(maxCnt)
    