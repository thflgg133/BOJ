H, M = map(int, input().split())
time = H*60+M-45
print(time//60%24, time%60)