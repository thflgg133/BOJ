def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def solution(n):
    list = prime_list(n) # prime_list 함수로 2 ~ n 까지 소수들이 어떤게 존재 하는지 알려줌
    idx = max([i for i in range(len(list)) if list[i] <= n/2]) # n/2 보다 작은 수 중 가장 큰 소수 찾기
    for i in range(idx,-1,-1): # 만약 idx값인 list[idx] + A 에서 A가 소수가 아니면 해당하지 않는 경우이므로 인덱스값 -1 해서 다시 진행
        for j in range(i, len(list)):  # list[idx] + j == n 을 만족할시 return문 실행
            if list[i] + list[j] == n:
                return "{} {}".format(list[i],list[j])

while True:
    T = int(input())
    for _ in range(T):
        n = int(input())
        run = print(solution(n))
    
    if T:
        break


'''
ex) 
8 = 3 + 5
10 = 5 + 5
16 = 5 + 11
100 = 47 + 53
'''
        
