import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    cmd = sys.stdin.readline().split()
    order = cmd[0]

    if len(cmd) == 1:
        if order == "all":
            S = set([i for i in range(1,21)])

        else:
            S = set()
    else:
        x = int(cmd[1])
        
        if order == "add":
            S.add(x)

        elif order == "remove":
            S.discard(x)

        elif order == "check":
            print(1 if x in S else 0)

        elif order == "toggle":
            if x in S:
                S.discard(x)

            else:
                S.add(x)