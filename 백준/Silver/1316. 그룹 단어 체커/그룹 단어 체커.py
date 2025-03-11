n = int(input())
result = 0

# 입력받기 방법 1
arr = []
for i in range(n):
    arr.append(input())

# 입력받기 방법 2
# arr = list(input().split())


# 시작
for i in range(n):
    x = arr[i]
    k = 0  # imsi에 들어갈 중복된 알파벳 개수
    imsi = [] # 중복된 알파벳이 들어갈 배열

    imsi.append(arr[i]) # 첫번째 알파벳 배열에 넣기

    for j in range(len(x)):
        if x[j] == imsi[k]: # 이전 알파벳이랑 같다면
            continue
        elif x[j] in imsi:
            k=-1
            break
        else:
            k+=1
            imsi.append(x[j])
    
    if k!=-1:
        result+=1


print(result)