def hanoi(n, start, another, to):  # n개의 원반, 시작 지점, 다른 지점, 도착 지점
    if n == 1:  # 탈출 조건
        print(start, to)
        return

    hanoi(n - 1, start, to, another)
    print(start, to)
    hanoi(n - 1, another, start, to)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 2, 3)
