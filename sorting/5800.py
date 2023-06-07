import sys;input=sys.stdin.readline

K=int(input())
for i in range(K):
    li=list(map(int,input().split()))
    del li[0]
    li.sort(reverse=True)
    Max=li[0]
    Min=li[-1]
    LarGap=0
    for j in range(len(li)-1):
        nowGap=(li[j]-li[j+1])
        if nowGap > LarGap:
            LarGap=nowGap

    print(f'Class {i+1}')
    print(f'Max {Max}, Min {Min}, Largest gap {LarGap}')
