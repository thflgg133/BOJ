import sys

N, M = map(int, sys.stdin.readline().split())

site_password = {}

for _ in range(N):
    site, password = sys.stdin.readline().split()
    site_password[site] = password # key value 를 활용해 사이트에 해당하는 비밀번호를 담음

for _ in range(M):
    want_site = sys.stdin.readline().rstrip() # \n 을 제거하기 위해 rstrip() 사용
    print(site_password[want_site]) # 원하는 사이트(key)의 비밀번호(value) 출력