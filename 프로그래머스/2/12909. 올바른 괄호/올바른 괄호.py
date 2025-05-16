def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    sum=0
    for i in s:
        if i=='(':
            sum+=1
        elif i==')':
            sum-=1
        if sum<0:
            answer=False
            break
    if sum!=0:
        answer=False
    return answer