import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    x = input().strip().split()

    if x[0] == '1':
        stack.append(int(x[1]))
    elif x[0] == '2':
        if not stack:
            print("-1")
        else:
            print(stack.pop())
    elif x[0] == '3':
        print(len(stack))
    elif x[0] == '4':
        if not stack:
            print("1")
        else:
            print("0")
    elif x[0] == '5':
        if not stack:
            print("-1")
        else:
            print(stack[-1])
