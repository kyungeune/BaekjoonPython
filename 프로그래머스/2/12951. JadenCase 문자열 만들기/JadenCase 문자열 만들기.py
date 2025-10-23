def solution(s):
    answer = ''
    
    for i in s.split(' '):
        answer+=i.capitalize()
        answer+=" "
    
    answer = answer[:-1]
    return answer