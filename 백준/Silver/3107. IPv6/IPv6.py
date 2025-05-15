import sys
from collections import deque

input=sys.stdin.readline

ip = list(input().strip().split(':'))

if (len(ip)==1) or (len(ip)==2 and ip[0]=='' and ip[1]=='') or (len(ip)==3 and ip[0]=='' and ip[1]=='' and ip[2]==''):  # 입력이 0인경우
    for i in range(8):
        if i==7:
            print('0000')
        else:
            print('0000',end=':')
    quit()

#print(ip)
namuzi = 9 - len(ip)
temp = 0
cnt=0
for i in ip:
    cnt+=1
    if i=='':
        if temp==1:  # ''이 하나의 개수로 인식되기 때문에 0000 별도로 추가해줘야 함
            if i==ip[len(ip)-1]:  # 근데 ::가 마지막에 있으면..
                print('0000')
            else:
                print('0000', end=':')
            continue

        for _ in range(namuzi):
            print('0000', end=':')
        temp=1  # 이전이 ''였는데 바로오는거 막기 위해서..
    else:
        temp=0
        if cnt==len(ip):
            print(i.rjust(4,'0'))
        else:
            print(i.rjust(4,'0'),end=':')
        