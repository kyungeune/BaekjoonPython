import sys
input = sys.stdin.readline
write = sys.stdout.write

# wrute는 print보다 가볍고 버퍼링도 됨

n = int(input())
s = set()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        s.add(int(cmd[1]))

    elif op == "check":
        x = int(cmd[1])
        write("1\n" if x in s else "0\n")

    elif op == "empty":
        s.clear()

    elif op == "toggle":
        x = int(cmd[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif op == "remove":
        s.discard(int(cmd[1]))  # remove랑 달리, x가 없어도 그냥 넘어감

    elif op == "all":
        s = set(range(1,21))


# print문으로 출력하면 시간 차이가 많이 남
# for ans in out:
#     print(ans)