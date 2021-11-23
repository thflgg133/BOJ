import sys

n = int(sys.stdin.readline())
cnt = 1
num_list = []
answer = []
tmp = True

for _ in range(n):
    num = int(sys.stdin.readline())

    while cnt <= num: # 1부터 num 까지 생성
        num_list.append(cnt) 
        answer.append("+") 
        cnt += 1 
    
    if num_list[-1] == num: # num으로 들어온 수 까지 pop() 하고 - 출력
        num_list.pop()
        answer.append("-")

    else: # 오름차순 순인데 num_list[-1] 보다 이전 인덱스가 나오면 앞에 인덱스가 pop되므로 스택 순열 성립X
        tmp = False # ex) num_list = [3,4,5] / num = 3 일때 num_list 안에 있는 3에 도달하려면 4, 5가 pop되어야 하므로 오류

if tmp == False:
    print("NO")

else:
    print(*answer, sep="\n")