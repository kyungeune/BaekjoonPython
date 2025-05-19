import sys
import re # 부호까지 살릴 수 있는 연산자
# (별) 아이디어 : 처음 나오는 - 뒤에있는 것들 모두 괄호로 묶기 (별)



input = sys.stdin.readline

temp = input()
num = re.split(r'([+-])', temp) # ['55', '-', '50', '+', '40\n']
num[len(num)-1] = num[len(num)-1].split('\n')[0]

nums = []  # 숫자들 넣어두기
buho = []  # 부호들 넣어두기
buhoim = 0
for i in range(len(num)):
    x = num[i]
    if buhoim == 0:
        nums.append(int(x))
        buhoim = 1
    else:
        buho.append(x)
        buhoim = 0


# - 등장 전까지 계산
i = 0
x=nums[0]  # '-' 전에있는 값들 계산한 합
while i<len(buho):
    if buho[i]=='-':
        sum = nums[i+1]

        for j in range(i+1, len(buho)):
                if buho[j] == '+':
                    sum+=nums[j+1]
                else:
                    sum+=nums[j+1]  # 괄호를 적절히 치는거니까.. 걍 첫 - 뒤에는 다 더해버리면 되는거였따.
        x-=sum
        break
    else:
        x+=nums[i+1]
    i+=1

print(x)