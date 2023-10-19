import sys

N, M = map(int, sys.stdin.readline().rstrip().split())


site_password = dict(set())


for _ in range(N):
    site, password = sys.stdin.readline().rstrip().split()
    site_password[site] = password

for _ in range(M):
    want_site = sys.stdin.readline().rstrip()
    print(site_password[want_site])