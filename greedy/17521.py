import sys
input = sys.stdin.readline

n, W = map(int, input().split())
prices = [int(input()) for _ in range(n)]

coin = 0
for i in range(n):
    if i != (n-1) and prices[i] < prices[i+1]:
        buyCoinAmount = W//prices[i]
        coin += buyCoinAmount
        W -= prices[i]*buyCoinAmount
    else:
        sellMoneyAmount = coin*prices[i]
        coin = 0
        W += sellMoneyAmount

print(W)