import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    put = input().split()

    if put[0] == "push":
        imsi = int(put[1])
        stack.append(imsi)
    elif put[0] == "pop":
        if not stack:
            print("-1")
        else:
            print(stack.pop())
    elif put[0] == "size":
        print(len(stack))
    elif put[0] == "empty":
        print("1" if not stack else "0")
    elif put[0] == "top":
        if not stack:
            print("-1")
        else:
            print(stack[-1])
