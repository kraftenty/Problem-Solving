import sys

from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split(' '))


def bfs(a, b):
    q = deque()
    q.append((a, 1))
    while q:
        now, hop = q.popleft()
        if now == b:
            return hop

        if (now * 2) <= b:
            q.append((now * 2, hop + 1))
        if (now * 10 + 1) <= b:
            q.append((now * 10 + 1, hop + 1))

    return -1


result = bfs(A, B)
print(result)
