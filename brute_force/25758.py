import sys
input = sys.stdin.readline

N = int(input())
li = list(map(str, input().split(' ')))
li = list(set(li))
print(li)
res = []

for i in range(len(li)):
    for j in range(i+1, len(li)):
        tmp1 = max(li[i][0],li[j][1])
        tmp2 = max(li[j][0],li[i][1])
        res.append(tmp1)
        res.append(tmp2)

res = list(set(res))
res.sort()
print(len(res))
print(' '.join(res))