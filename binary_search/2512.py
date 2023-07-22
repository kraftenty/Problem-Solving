import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
M = int(input())

if sum(li) <= M:
    print(max(li))
else:
    # 이분 탐색
    start, end = 0, max(li)
    while start <= end:
        mid = (start + end) // 2

        sum_li = 0
        for elem in li:
            if elem >= mid:
                sum_li += mid
            else:
                sum_li += elem

        if sum_li > M:
            end = mid - 1
        else:
            start = mid + 1

    print(end)
