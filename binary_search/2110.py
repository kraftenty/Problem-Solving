import sys

input = sys.stdin.readline

def ableAPCount(dist):
    cnt = 1
    prevCoord = coord[0]
    for i in range(1, len(coord)):
        currentCoord = coord[i]
        if currentCoord - prevCoord >= dist:
            cnt += 1
            prevCoord = currentCoord
    return cnt

# 목표 : 가장 인접한 두 공유기 사이의 거리를 최대화
# 집의 개수 N, 설치해야 하는 공유기의 개수 C
N, C = map(int, input().split())
coord = [0] * N  # 집의 좌표 저장
for i in range(N):
    coord[i] = int(input())
coord.sort()

result = 0
lowDist, highDist = 1, (coord[N - 1] - coord[0])
while (lowDist <= highDist):
    midDist = (lowDist + highDist) // 2
    if ableAPCount(midDist) >= C:
        result = max(result, midDist)
        lowDist = midDist + 1
    else:
        highDist = midDist - 1


print(result)