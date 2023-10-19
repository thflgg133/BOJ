A,B,V = map(int, input().split())

total_day = (V-B)/(A-B)
print(total_day)
print(V-B)
print(A-B)

if int(total_day) != total_day:
    print(int(total_day)+1)

else:
    print(int(total_day))