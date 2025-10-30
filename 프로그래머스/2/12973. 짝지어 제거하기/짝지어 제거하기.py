def solution(s):
    answer = -1
    arr = []
    arr.append(s[0])
    a = 0
    
    for i in range(1, len(s)):
        if len(arr) > 0 and arr[a] == s[i]:
            a-=1
            arr.pop()
        else:
            a+=1
            arr.append(s[i])
    
    if len(arr) == 0:
        answer = 1
    else:
        answer = 0
    
    
    # b aa b aa / aababaabaaab
#     if len(s)%2 == 1:  # 총 개수가 홀수개이면 일단 거름
#         return 0
    
#     while len(s) > 0:  # 비어있지 않을 때까지!
        
#         for x in range(len(s)-1):  # 연속 일치할때까지 돌기
#             if s[x] == s[x+1]:
#                 break
#             if x == len(s)-1:  # 아예 일치하는게 없는건 여기서부터 거름
#                 return 0
                
        
#         if len(s) <= 2:  # 문자열 재조합이 더이상 불가능하면
#             if s[x] == s[x+1]:
#                 return 1
#             else:
#                 return 0
        
#         s = s[:x] + s[x+2:]
        
#     # while문 끝
    

    return answer