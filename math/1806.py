#누적 합, 투 포인터
import sys
INIT_MAX_LEN = 100001

# N = 수열의 길이, S = 수열에서 연속된 수들의 부분합 중 S 이상. 제일 짧은 것의 길이 구하기
N, S = map(int, input().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))

leftPtr, rightPtr = 0, 0
minLength = INIT_MAX_LEN

cumulativeSum = li[0]
while leftPtr <= rightPtr:
    # 총합이 S 이상일 때
    if cumulativeSum >= S:
        cumulativeSum -= li[leftPtr]
        minLength = min(minLength, rightPtr-leftPtr+1)
        leftPtr += 1
    # 총합이 S보다 모자랄 때
    else:
        rightPtr+=1
        if rightPtr==N:
            break
        cumulativeSum += li[rightPtr]

if minLength==INIT_MAX_LEN:
    print(0)
else:
    print(minLength)