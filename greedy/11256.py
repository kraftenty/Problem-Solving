import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    J, N = map(int ,input().split())
    boxes = []
    for _ in range(N):
        R, C = map(int ,input().split())
        boxes.append(R*C)
    
    boxes.sort(reverse=True)
    boxCnt = 0
    for box in boxes:
        J -= box
        boxCnt+=1
        if J<=0:
            break
    
    print(boxCnt)