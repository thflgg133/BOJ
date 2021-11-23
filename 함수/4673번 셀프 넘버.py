list = []
def d(N):
    for j in str(N):
        N += int(j)
    list.append(N)

for i in range(1,9994):
    d(i)
    if i not in list:
        print(i)
