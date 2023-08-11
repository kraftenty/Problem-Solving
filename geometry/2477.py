import sys
input=sys.stdin.readline

K = int(input())

horizontal = []
vertical = []
allCourse = []

maxHorizontalIndex=0
maxHorizontalValue=0
maxVerticalIndex=0
maxVerticalValue=0

for i in range(6):
    direction, length = map(int, input().split())
    if direction==1 or direction==2: # EAST or WEST
        if length > maxHorizontalValue:
            maxHorizontalValue = length
            maxHorizontalIndex = i
        horizontal.append(length)
    else:                            # SOUTH or NORTH
        if length > maxVerticalValue:
            maxVerticalValue = length
            maxVerticalIndex = i
        vertical.append(length)
    allCourse.append(length)

bigArea = max(horizontal) * max(vertical)

smallAreaHorizontalLength = allCourse[(maxVerticalIndex+3)%6]
smallAreaVerticalLength = allCourse[(maxHorizontalIndex+3)%6]

smallArea = smallAreaHorizontalLength * smallAreaVerticalLength

print((bigArea - smallArea) * K)
