import sys;input=sys.stdin.readline

dic=dict()
cnt=0
while True:
    species=input().rstrip()
    if species=='':
        break

    cnt+=1
    if species in dic:
        dic[species]+=1
    else:
        dic[species]=1

sorted_dic=dict(sorted(dic.items()))
for key,val in sorted_dic.items():
    print('%s %.4f'%(key,(val/cnt)*100))