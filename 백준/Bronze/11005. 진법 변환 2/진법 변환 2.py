x, n = input().split() # x를 n진법으로

x = int(x)
n = int(n)  
result = []

while x >= 1:
    if x==1 or x==0:
        result.append(x)
        break
    nam = 0
    nam = x % n
    x = x // n
    result.append(nam)

for i in reversed(range(len(result))):
    if result[i] >= 10:
        print(chr(result[i]+55), end='')
    else:
        print(result[i], end='')