import sys;input=sys.stdin.readline

K,L = map(int,input().split())
dic=dict()
for i in range(L):
    dic[input().rstrip()]=i

sortedLi = sorted(dic.items(), key=(lambda x: x[1]))
sortedLiLen=len(sortedLi)
for i in range(K):
    if i>=sortedLiLen:
        break
    print(sortedLi[i][0])