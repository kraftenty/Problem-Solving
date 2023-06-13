import sys;input=sys.stdin.readline
N=int(input())
s = set()
for n in range(N):
    name,cmd = input().split()
    if cmd=="enter":
        s.add(name)
    else:
        s.remove(name)

li=list(s)
li.sort(reverse=True)
print('\n'.join(li))