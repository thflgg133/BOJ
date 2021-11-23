A,V,B = map(int, input().split())

total_day = (B-V)/(A-V)


if int(total_day) != total_day:
    print(int(total_day)+1)

else:
    print(int(total_day))