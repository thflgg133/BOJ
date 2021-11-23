import sys

n = int(sys.stdin.readline())
cnt = 1
num_list = []
answer = []
tmp = True

for _ in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        num_list.append(cnt)
        answer.append("+")
        cnt += 1
    
    print(num_list)

    if num_list[-1] == num:
        num_list.pop()
        answer.append("-")

    else:
        tmp = False

if tmp == False:
    print("NO")

else:
    for i in answer:
        print(i)