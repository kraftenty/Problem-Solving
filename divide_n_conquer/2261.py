import sys
input = sys.stdin.readline

n = int(input())
S = [list(map(int,input().split(' '))) for _ in range(n)]
S.sort(key=lambda x: x[0])

def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def ClosestPair(start, end):
    if end-start == 1:
        return dist(S[start], S[end])
    
    mid = (start + end) // 2
    d = min(ClosestPair(start, mid), ClosestPair(mid, end))

    S_new = []
    for i in range(start, end + 1):
        if (S[mid][0] - S[i][0])**2 < d:
            S_new.append(S[i])

    S_new.sort(key=lambda x:x[1])

    for i in range(len(S_new)-1):
        for j in range(i+1, len(S_new)):
            if (S_new[i][1] - S_new[j][1])**2 >= d:
                break
            d = min(d, dist(S_new[i], S_new[j]))

    return d


print(ClosestPair(0, n-1))