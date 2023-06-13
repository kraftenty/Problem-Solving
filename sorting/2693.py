import sys;input=sys.stdin.readline
T=int(input())
for t in range(T):
    li=list(map(int,input().split()))
    print(sorted(li)[-3])
