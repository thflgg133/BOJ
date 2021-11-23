import sys

T = int(sys.stdin.readline())
model = [1, 2, 4]

for i in range(3, 10):
    model.append(model[i - 3] + model[i - 2] + model[i - 1])

for _ in range(T):
    num = int(sys.stdin.readline())
    print(model[num - 1])
    