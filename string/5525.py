import sys

input = sys.stdin.readline

# P1 = IOI
# P2 = IOIOI
# P3 = IOIOIOI
# ...

N = int(input())  # PN
M = int(input())  # S의 길이
S = input().rstrip()

cnt = 0
lptr, rptr = 0, 0
while rptr < M:
    try:
        if S[rptr] == 'I':  # I
            rptr += 1
            if S[rptr] == 'O':  # IO
                rptr += 1
                if S[rptr] == 'I':  # IOI
                    if (rptr - lptr) == (N * 2):
                        lptr += 2
                        cnt += 1
                else:  # IOO
                    rptr += 1
                    lptr = rptr

            else:  # II
                lptr = rptr

        else:  # O
            rptr += 1
            lptr = rptr
    except:
        break

print(cnt)
