original, n = input().split()

n = int(n) # int로 변환
result = 0
gop = 1 # n진수를 위해 각 자릿수마다 곱해줄...

for i in reversed(range(len(original))):
    x = original[i] # 활용하기 쉽게 변수에 저장

    if x.isalpha():
        x = ord(x) - 55
    
    x = int(x)

    result += x * gop
    gop *= n

print(result)