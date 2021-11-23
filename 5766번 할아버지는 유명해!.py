import sys

while True:
    player = [[0,i] for i in range(10001)] # [0은 점수, i는 번호] 몇번째 선수인지 알기 위해 만든 리스트 10000번까지 있지만 
                                           # 0 ~ 10000번까지 10001개 만드는 이유는 리스트의 처음 인덱스는 0이기 떄문
    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0:
        break

    for _ in range(N):
        for i in map(int, sys.stdin.readline().split()):
            player[i][0] += 1 # 특정 번호의 선수가 랭킹에 올라온다면 점수 +1 
    
    player.sort(reverse=True, key=lambda x: [x[0], -x[1]]) # 점수는 높은 순 등수는 낮은 순으로 정렬 오름차순으로 출력해야 하기 떄문
    second_score = player[1][0] # 등수가 2등인 선수는 점수순으로 정렬했을때 두번째 인덱스에 위치한 사람
    second_place = [player[1][1]] # 2등인 선수의 번호를 second_place 리스트에 담음
    
    for i in range(2,10001): 
        if player[i][0] == second_score: # 등수가 2등인 선수는 동점이라 여러명 존재 할 수 있으니 탐색해서 점수가 같은 사람들도 다 포함시킴
            second_place.append(player[i][1])

        else:
            break

    print(*second_place) # *를 통해 second_place 리스트에 있는 값 전부 공백을 두고 출력
