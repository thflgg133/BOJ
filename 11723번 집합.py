import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    cmd = sys.stdin.readline().split()
    order = cmd[0] # 명령어

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
                S.discard(x) # set() 에서는 list와 다르게 remove() 함수 가 아닌 discard() 함수를 사용한다

            else:
                S.add(x) # set() 에서는 list와 다르게 append() 함수 가 아닌 add() 함수를 사용한다