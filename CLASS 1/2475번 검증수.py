Test_num = list(map(int, input().split()))
total = 0

for i in range(len(Test_num)):
    total += Test_num[i] ** 2

print(total % 10)