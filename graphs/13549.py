from collections import deque

N, K = map(int, input().split())


def bfs(start, dest):
    dq = deque()
    dq.append(start)
    time = [-1] * (100001)
    time[start] = 0

    while dq:
        now = dq.popleft()
        # 종료 조건
        if now == dest:
            return time[now]
        # 순간이동(곱하기2)
        if 0 <= now * 2 <= 100000 and time[now * 2] == -1:
            time[now * 2] = time[now]
            dq.appendleft(now * 2)

        # 한칸 마이너스
        if 0 <= now - 1 <= 100000 and time[now - 1] == -1:
            time[now - 1] = time[now] + 1
            dq.append(now - 1)
        # 한칸 플러스
        if 0 <= now + 1 <= 100000 and time[now + 1] == -1:
            time[now + 1] = time[now] + 1
            dq.append(now + 1)



print(bfs(N, K))
