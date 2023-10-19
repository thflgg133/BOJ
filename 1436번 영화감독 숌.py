import sys 

N = int(sys.stdin.readline())
cnt = 0
END_num = 666 # 666 이전의 숫자는 고려할 필요 X

while True:
    if '666' in str(END_num):
        cnt += 1

    if cnt == N:
        print(END_num)
        break

    END_num += 1 # 브루트 포스 개념 적용, END_num에 1씩 더해가면서 계속 666이 숫자안에 들어있는지 탐색