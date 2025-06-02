import sys

def is_balanced(s):
    stack = []
    for char in s:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    print("yes" if is_balanced(line) else "no")
