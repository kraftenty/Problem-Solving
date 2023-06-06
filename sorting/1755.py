import sys
input=sys.stdin.readline
# eight , five, four, nine, one, seven, six, three, two, zero 
order=[8,5,4,9,1,7,6,3,2,0] 

save=list()
for i in order:
    save.append(i)
    if i==0:
        break
    for j in order:
        save.append(i*10 + j)

M,N=map(int,input().split())
cnt=0
for s in save:
    if M<=s<=N:
        print(s, end=' ')
        cnt+=1
        if cnt%10==0:
            print()