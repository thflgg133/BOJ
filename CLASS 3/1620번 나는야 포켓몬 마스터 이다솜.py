import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dict = {}


for i in range(1,N+1):
    pokemon_name = sys.stdin.readline()
    pokemon_dict[pokemon_name] = i

pokemon_key = list(pokemon_dict.keys())

for _ in range(M):
    pokemon = sys.stdin.readline()

    if pokemon in pokemon_dict.keys():
        print(pokemon_dict[pokemon], end = "\n")

    else:
        print(pokemon_key[int(pokemon)-1], end = "")