import sys

N = int(sys.stdin.readline())
queue_list = []

for _ in range(N):
    cmd = sys.stdin.readline().split()
    order = cmd[0]

    if order == "push":
        queue_list.append(cmd[1])

    elif order == "pop": 
        if queue_list == []:
            print(-1)

        else:
            print(queue_list.pop(0))

    elif order == "size":
        print(len(queue_list))

    elif order == "empty":
        if queue_list == []:
            print(1)
        
        else:
            print(0)

    elif order == "front":
        if queue_list == []:
            print(-1)

        else:
            print(queue_list[0])

    elif order == "back":
        if queue_list == []:
            print(-1)

        else:
            print(queue_list[-1])
