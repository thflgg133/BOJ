def erase_star(n) : #별로 채워진 Map에서 조건에 해당되는 영역을 빈공간으로 지움
    global Map # 별로 채워진 Map을 가져오기 위해 전역 변수 설정 
    a = n // 3
    if n == 3:
        Map[1][1] = " "
        for i in range(N//3):
            for j in range(N//3):
                Map[1+i*3][1+j*3] = Map[1][1]
          
        return
    
    if n == N:
        for i in range(n):
            for j in range(n): # a == 9 , a == 3
                if  (1 <= i // a and i // a < 2) and (1 <= j // a and j // a < 2) :
                    Map[i][j] = " "
               
        return erase_star(a)
    
    if 3 < n < N:
        global cnt
        for i in range(n):
            for j in range(n): # a == 9 , a == 3
                    if  (1 <= i // a and i // a < 2) and (1 <= j // a and j // a < 2) :
                        Map[i][j] = " "
                        for k in range(3**cnt):
                            for l in range(3**cnt):
                               Map[i+n*k][j+n*l] = Map[i][j]
        cnt +=1
        return erase_star(a)
    

N = int(input())   
cnt = 1  
Map = [["*" for i in range(N)] for i in range(N)] # N X N 영역의 공간 생성 그안의 value값은 별로 이루어져있음

erase_star(N)

for i in Map: # 결과 출력
    for j in i:
        print(j, end = "")

    print()

# print('\n'.join([j for j in i]) for i in Map])) List Comprehension


'''
n = 3 일 때 (1,1) 빈 공간 n // 3^0 == 1 일때
n = 9 일 때 (3,3) ~ (5,5) 빈 공간 n // 3^1 == 1 일때 
n = 27 일 때 (9,9) ~ (17, 17) 빈 공간 n // 3^2 == 1 일때 
'''