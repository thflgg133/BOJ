N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt += (N//5)
        print(cnt)
        break

    elif N < 0:
        print("-1")
        break
    
    N -= 3
    cnt += 1
