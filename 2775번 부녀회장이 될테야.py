t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    people_list = [x for x in range(1, n+1)]
   
    for floor in range(k):
        for row in range(1, n):
            people_list[row] += people_list[row-1]
       
    print(people_list[-1])