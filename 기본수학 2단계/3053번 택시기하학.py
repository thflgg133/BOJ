import math
r = int(input())
print("{:6f}".format(r*r*math.pi))
print("{:6f}".format(2*r*r))

# 사실 소수점6째짜리 까지 나타낼 필요는 없음
# WHY? 0.000001까지 오차는 바준다했으니 뒤에도 표헌해도 상관 X