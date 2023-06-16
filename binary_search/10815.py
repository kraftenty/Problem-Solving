import sys;input=sys.stdin.readline
N=int(input())
cards=list(map(int,input().split()))
cards.sort()
M=int(input())
query=list(map(int,input().split()))

def bin_search(x):
    l=0
    r=N-1
    while(l<=r):
        m=(l+r)//2
        if x < cards[m]:
            r=m-1
        elif x > cards[m]:
            l=m+1
        else:
            return True
    return False
        

for q in query:
    res=bin_search(q)
    if res:
        print(1,end=' ')
    else:
        print(0,end=' ')
    