class Wheel:
    def __init__(self, length):
        self.li = ['?' for _ in range(length)]
        self.now = 0
        self.failFlag = False
    def rotate(self, tick):
        self.now = (self.now + tick) % len(self.li)
    def put(self, ch):
        if self.li[self.now] != '?' and ch != self.li[self.now]:
            self.failFlag = True
        if ch in self.li and ch != self.li[self.now]:
            self.failFlag = True
        self.li[self.now] = ch
    def print(self):
        if self.failFlag:
            print('!')
        else:
            for i in range(self.now, self.now - len(self.li), -1):
                print(self.li[i], end='')



N, K = map(int, input().split())
wheel = Wheel(N)
for _ in range(K):
    S, C = map(str, input().split())
    wheel.rotate(int(S))
    wheel.put(C)

wheel.print()

