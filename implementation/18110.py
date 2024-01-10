import sys


def myRound(num):
    return int(num + 0.5)


def main():
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        return 0
    li = [0] * n
    for i in range(n):
        li[i] = int(sys.stdin.readline().rstrip())

    li.sort()

    cutNum = myRound(n * 0.15)

    sum = 0
    for i in range(cutNum, n - cutNum):
        sum += li[i]

    return myRound(sum / (n - cutNum * 2))


if __name__ == "__main__":
    res = main()
    print(res)
