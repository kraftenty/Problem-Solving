import sys;input=sys.stdin.readline

N=input().rstrip()
arr=[0 for _ in range(11)]
for n in N:
    tmp=int(n)
    if tmp==6 or tmp==9:
        if arr[6] <= arr[9]:
            arr[6]+=1
        else:
            arr[9]+=1
    else:
        arr[tmp]+=1

print(max(arr))