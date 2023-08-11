import sys

input = sys.stdin.readline

N = int(input())
li = list()
for _ in range(N):
    li.append(list(map(int, input().split(' '))))

# DP
# li[i][0]: R색상
# li[i][1]: G색상
# li[i][2]: B색상
resultList = []
maxValue = 10000001
for startColor in range(3):  # R, G, B
    # tempLi 설정
    tempLi = [[0] * 3 for _ in range(N)]
    tempLi[0] = [1001, 1001, 1001]
    tempLi[0][startColor] = li[0][startColor]

    for i in range(1, N):
        tempLi[i][0] = min(tempLi[i - 1][1], tempLi[i - 1][2]) + li[i][0]
        tempLi[i][1] = min(tempLi[i - 1][0], tempLi[i - 1][2]) + li[i][1]
        tempLi[i][2] = min(tempLi[i - 1][0], tempLi[i - 1][1]) + li[i][2]
    tempLi[N - 1][startColor] = maxValue
    resultList.append(min(tempLi[N - 1]))

print(min(resultList))
