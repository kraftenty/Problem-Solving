import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    funcStr=input().rstrip()
    n=int(input())
    dq=deque(input().rstrip()[1:-1].split(','))
    rev=0
    Error=False

    if n==0:
        dq=[]
    
    for f in funcStr:
        if f=='R': # R
            rev+=1
        else: # D
            if len(dq)==0:
                Error=True
                break
            if rev%2==0: # straight
                dq.popleft()
            else: # reversed
                dq.pop()
    
    if not Error:
        print('[',end='')
        if rev%2==0: # straight
            while dq:
                print(dq.popleft(), end= ',' if len(dq)>0 else '')
        else: # reversed
            while dq:
                print(dq.pop(),end= ',' if len(dq)>0 else '')
        print(']')
    else:
        print('error')