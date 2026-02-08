def solution(phone_book):
    answer = True
    phone_book.sort()
    length = len(phone_book)
    
    for i in range(length - 1):
        x = phone_book[i]
        total = 0
        if phone_book[i + 1].startswith(x):
            return False
    
    return answer