import sys;input=sys.stdin.readline

dp=[0 for _ in range(100)]

def fibo(n):
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

N=int(input())
print(fibo(N))