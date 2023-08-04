import sys
input = sys.stdin.readline

zeroCountList=[1, 0]
oneCountList=[0, 1]
def fibo(n):
    if n >= len(zeroCountList):
        for i in range(len(zeroCountList), n + 1, 1):
            zeroCountList.append(zeroCountList[i - 1] + zeroCountList[i - 2])
            oneCountList.append(oneCountList[i - 1] + oneCountList[i - 2])
    return zeroCountList[n], oneCountList[n]

T=int(input())
for _ in range(T):
    N = int(input())
    zeroCount, oneCount = fibo(N)
    print(f'{zeroCount} {oneCount}')