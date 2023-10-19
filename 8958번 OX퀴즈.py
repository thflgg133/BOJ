answer = 0
count = 1
list = []
M = int(input())
for i in range(M):
    Test_case = input()
    list.append(Test_case)

for Test_case in list:
    for ox in range(len(Test_case)):
        if Test_case[ox] == 'O':
            answer += count
            count += 1

        if Test_case[ox] == 'X':
            count = 1
    
    print(answer)
    count = 1
    answer = 0


