import sys;input=sys.stdin.readline

def sumNumInStr(s):
    sum=0
    for ch in s:
        if ch.isdigit():
            sum+=int(ch)
    return sum

class Guitar:
    def __init__(self,serial):
        self.serial=serial
    def __lt__(self,other): # <
        if len(self.serial) != len(other.serial):
            return len(self.serial) < len(other.serial)
        else:
            selfSumNum=sumNumInStr(self.serial)
            otherSumNum=sumNumInStr(other.serial)
            if selfSumNum != otherSumNum:
                return selfSumNum < otherSumNum
            else:
                return self.serial < other.serial

N=int(input())
Guitars=list()
for n in range(N):
    Guitars.append(Guitar(input().rstrip()))
Guitars.sort()
for g in Guitars:
    print(g.serial)