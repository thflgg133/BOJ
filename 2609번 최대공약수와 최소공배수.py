a, b = map(int, input().split())

def gcd(x,y): # 최대공약수(유클리드 호재법)
    mod = x % y 
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y    
    
def lcm(x, y): # 최소공배수
    return x * y // gcd(x,y) # 두 수를 곱하고 최대공약수로 나눈 값 == 최소공배수

print(gcd(a, b))
print(lcm(a, b))