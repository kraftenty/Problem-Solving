import sys
input=sys.stdin.readline

li = [0]

A, B = map(int, input().split())
for i in range(1, B+1):
    for j in range(i):
        li.append(i)

res = sum(li[A:B+1])
print(res)