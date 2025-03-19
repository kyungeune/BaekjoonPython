n = int(input())

rslt = 0
for i in range(n-9*len(str(n)), n):
    sum = 0  # 각 자리를 이루고 있는 숫자들 저장
    k = i

    while k >= 1:
        sum += int(k%10)
        k /= 10

    if sum + i == n:
        rslt = i
        break  # 가장 작은 생성자를 구해야 하기 때문, 가장 큰 생성자일 경우 break를 삭제

print(rslt)