N= int(input())
cnt = 0
END_num = 666
while True:
    if '666' in str(END_num):
        cnt += 1
    if cnt == N:
        print(END_num)
        break
    END_num += 1