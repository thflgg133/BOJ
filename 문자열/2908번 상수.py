n1,n2 = input().split()

if n1[::-1] > n2[::-1]:
    print(n1[::-1])

else:
    print(n2[::-1])

'''
print(max([int(num[::-1]) for num in input().split()]))
'''