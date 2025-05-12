import sys
input = sys.stdin.readline

n, m = map(int,input().split())
visited=[False]*(n+1)
result=[]

def backtrack(d):
    if d==m:
        ans = ''
        for i in result:
            ans+=str(i) + ' '
        print(ans.strip())
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i]=True
            result.append(i)
            backtrack(d+1) # 다음 숫자 재귀호출
            # 다음 숫자를 시도하기 위해서
            result.pop()
            visited[i]=False

backtrack(0)