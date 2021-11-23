import sys

x, y = map(int, sys.stdin.readline().split())

calender = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7: 31, 8:31, 9:30, 10:31, 11:30, 12:31}

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

total_days = 365

for i in range(12, x, -1):
    total_days -= calender[i]

total_days -= (calender[x] -y)

day = days[total_days % 7]

print(day)