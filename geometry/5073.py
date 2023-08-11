import sys
input=sys.stdin.readline

while True:
    li = list(map(int, input().split(' ')))
    li.sort()
    a, b, c = li[0], li[1], li[2]

    if a==b==c==0:
        break

    if c >= (a + b):
        print('Invalid')

    elif a==b==c:
        print('Equilateral')
    
    elif a==b or b==c or a==c:
        print('Isosceles')
    
    else:
        print('Scalene')