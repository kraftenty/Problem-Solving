import sys
input=sys.stdin.readline

N=int(input())
for _ in range(N):
    numberPlate=list(input().rstrip().split('-'))
    firstPart, secondPart = numberPlate[0], numberPlate[1]
    firstPartValue, secondPartValue = 0, int(secondPart)

    for i, ch in enumerate(firstPart):
        firstPartValue += ((ord(ch) - ord('A')) * (26 ** (2-i)))

    if abs(firstPartValue - secondPartValue) <= 100:
        print('nice')
    else:
        print('not nice')

