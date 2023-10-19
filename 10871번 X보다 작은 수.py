a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))