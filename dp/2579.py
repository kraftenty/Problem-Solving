import sys

input = sys.stdin.readline

totalNum = int(input())
stairs = list()
for i in range(totalNum):
    stairs.append(int(input()))

dp = [0] * totalNum

if len(stairs) <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, totalNum):
        # i-3 i-2 i-1 i
        #  o   x   o  o
        #  x   o   x  o
        oneHop = dp[i-3] + stairs[i-1] + stairs[i]
        twoHop = dp[i-2] + stairs[i]
        dp[i] = max(oneHop,twoHop)
    print(dp[-1])