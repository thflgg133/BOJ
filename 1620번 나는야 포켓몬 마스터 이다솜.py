import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dict = {}

for number in range(1,N+1):
    pokemon_name = sys.stdin.readline()
    pokemon_dict[pokemon_name] = number # key = pokemon_name, value = number

pokemon_key = list(pokemon_dict.keys()) # 번호로 포켓몬을 찾을 때를 위해 pokemon_key 생성

for _ in range(M):
    pokemon = sys.stdin.readline()

    if pokemon in pokemon_dict.keys(): # 포켓몬 이름으로 들어올 때
        print(pokemon_dict[pokemon], end = "\n")

    else: # 번호로 들어올 때
        print(pokemon_key[int(pokemon)-1], end = "")