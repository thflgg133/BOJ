import sys

T = int(sys.stdin.readline())
model = [1, 2, 4] # 3번째 경우까지는 직접 생성

for i in range(3, 10): # n은 10까지 이므로
    model.append(model[i - 3] + model[i - 2] + model[i - 1]) # 4부터 ~ n까지는 그 전, 전전, 전전전단계 경우의 수의 총합이다. 
                                                             # ex) model[4] = model[1] + model[2] + model[3] = 1 + 2 + 4 = 7
for _ in range(T):
    num = int(sys.stdin.readline())
    print(model[num - 1])