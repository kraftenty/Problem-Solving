import sys;input=sys.stdin.readline

T=int(input())
for t in range(T):
    A,B=input().split()
    if sorted(A) == sorted(B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')