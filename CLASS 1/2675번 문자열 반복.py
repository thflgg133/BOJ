T = int(input())

for i in range(T):
    R, S = input().split()
    text = ""
    for i in S:
        text += i*int(R)

    print(text)
