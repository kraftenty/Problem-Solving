k = int(input())
k = 2**k
xinit, yinit = map(int, input().split())
xinit -= 1; yinit -= 1

li = [[0 for _ in range(k)] for _ in range(k)]
li[yinit][xinit] = -1

def isThereNoHole(size, sy, sx):
    for y in range(sy, sy+size):
        for x in range(sx, sx+size):
            if li[y][x] != 0:
                return False
    return True

numbering = 0
def func(size, sy, sx):
    global numbering
    numbering += 1
    halfSize = size // 2

    if isThereNoHole(halfSize, sy, sx + halfSize):
        li[sy + halfSize - 1][sx + halfSize] = numbering
    if isThereNoHole(halfSize, sy, sx):
        li[sy + halfSize - 1][sx + halfSize - 1] = numbering
    if isThereNoHole(halfSize, sy + halfSize, sx):
        li[sy + halfSize][sx + halfSize - 1] = numbering 
    if isThereNoHole(halfSize, sy + halfSize, sx + halfSize): 
        li[sy + halfSize][sx + halfSize] = numbering 

    if halfSize == 1:
        return

    func(halfSize, sy, sx + halfSize)
    func(halfSize, sy, sx)
    func(halfSize, sy + halfSize, sx)
    func(halfSize, sy + halfSize, sx + halfSize)


func(k, 0, 0)
for i in range(k-1, -1, -1):
    for j in range(k):
        print(li[i][j], end=' ')
    print()