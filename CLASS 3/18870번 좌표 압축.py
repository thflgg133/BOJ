import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_list = list(sorted(set(num))) # set을 사용해 중복된 수 제거
num_list = {num_list[i] : i for i in range(len(num_list))} # 작은 수 부터 순서를 dictionary형태로 매긴다
print(*[num_list[i] for i in num]) # *을 이용해 unpacking해 출력