words = input().upper()
words_types = list(set(words))
tmp = []

for i in words_types:
    cnt = words.count(i)
    tmp.append(cnt)

if tmp.count(max(tmp)) > 1:
    print("?")

else:
    max_index = tmp.index(max(tmp))

    print(words_types[max_index])

'''
n = input().upper()
t= []
for i in set(n):
    t.append(n.count(i))
idx = [i for i,x in enumerate(t) if x == max(t)]
if len(idx) >1:
    print("?")

else:
    print(list(set(n))[t.index(max(t))])
'''