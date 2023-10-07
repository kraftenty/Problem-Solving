import sys
import itertools
input=sys.stdin.readline

N, S = map(int,input().split())
li = list(map(int, input().split()))

res = 0
for i in range(1, N+1):
    combi_lis = itertools.combinations(li, i)
    for combi_li in combi_lis:
        if sum(combi_li)==S:
            res+=1

print(res)