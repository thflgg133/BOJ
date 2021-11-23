x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

list1 = [x1, x2, x3]
list2 = [y1, y2, y3]

x4 = [i for i in list1 if list1.count(i) == 1]
y4 = [j for j in list2 if list2.count(j) == 1]

print(x4[0], y4[0])