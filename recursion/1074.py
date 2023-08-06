import sys
input = sys.stdin.readline

N, r, c = map(int,input().split())
count=0


def func(size, y, x):
    global count
    halfSize = size // 2

    # Z의 1번째 면
    if y < halfSize and x < halfSize:
        if halfSize == 1:
            print(count)
            sys.exit(0)
        func(halfSize, y, x)
    
    # Z의 2번째 면
    elif y < halfSize and x >= halfSize:
        if halfSize == 1:
            print(count + 1)
            sys.exit(0)
        count += halfSize**2 * 1
        func(halfSize, y,  x - halfSize)

    # Z의 3번째 면
    elif y >= halfSize and x < halfSize:
        if halfSize == 1:
            print(count + 2)
            sys.exit(0)
        count += halfSize**2 * 2
        func(halfSize, y - halfSize, x)
    
    # Z의 4번째 면
    elif y >= halfSize and x >= halfSize:
        if halfSize == 1:
            print(count + 3)
            sys.exit(0)
        count += halfSize**2 * 3
        func(halfSize, y - halfSize, x - halfSize)

func(2 ** N, r, c)