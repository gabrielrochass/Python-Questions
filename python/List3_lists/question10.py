# encontrar pistas
# pista = duas matrizes quadradas
# pista x pista = matriz -> diagonal = y
#pista + pista = matriz -> somatorio = x

#matriz 8x8
#move primeiro na vertical dps na horizontal
#nao pode andar na diagonal

# mapa = lista de lista(matriz)

#esq_temp = horontal ->
#direcao x -1 quando chega na borda = volta

#policia = horizontal e dps vertical

police = [0,0]
p_team = [0,0]
me = [0,0]
direcao = 1
steps_p = 0
estado = 0

xy = input().split()
me[0] = int(xy[1])
me[1] = int(xy[0])
xy = input().split()
p_team[0] = int(xy[1])
p_team[1] = int(xy[0])

for loc in range(3):
  # print(estado)
  location = [0,0]
  steps = 0
  location_name = input()
  if loc == 2:
    xy = input().split()
    police[0] = int(xy[1])
    police[1] = int(xy[0])
  num_matriz = int(input())
  matrizes = [[],[]]
  for j in range(2):
    for k in range(num_matriz):
      linha = input().split()
      matrizes[j].append([])
      for it in linha:
        matrizes[j][k].append(int(it))
        location[1] += int(it)
        
  #print(matrizes)
  for i in range(num_matriz):
    for j in range(num_matriz):
      location[0] += matrizes[0][i][j]*matrizes[1][j][i]
  
  dif = abs(me[0] - location[0])
  minha_direcao = 1
  if location[0] - me[0]< 0:
    minha_direcao = -1
  if p_team[1] == 0:
    direcao = -1
  for i in range(dif): 
    if p_team[1] == 0 or p_team[1] == 7: 
      direcao *= -1
    p_team[1] += direcao
    me[0] += minha_direcao
    steps += 1
    if p_team[1] == me[1] and p_team[0] == me[0]:
      estado = 3
    
  if p_team[0] == me[0] and p_team[1] == me[1]: 
    estado = 3
    
  if estado != 3:
    dif = abs(me[1] - location[1])
    minha_direcao = 1
    if location[1] - me[1] < 0:
      minha_direcao = -1
    for i in range(dif): 
      if p_team[1] == 0 or p_team[1] == 7: 
        direcao *= -1
      p_team[1] += direcao
      me[1] += minha_direcao
      steps += 1
      if p_team[1] == me[1] and p_team[0] == me[0]:
        estado = 3
      # break
  # print(estado)
  # print(loc)
  if loc == 2:
    steps_p += abs(police[0] - location[0]) + abs(police[1] - location[1])
    if steps_p < steps:
      estado = 2
    else:
      estado = 1
  if estado == 0 or estado == 1:
    # print("hoi")
    print(f"{location_name} está na coluna {location[1]} e na linha {location[0]}. Foram dados {steps} passos para chegar lá.")
  else:
    break
# print(1)


if estado == 1:
  print("IUHU, VOCÊ SALVOU O FORD!! Agora, todos podem voltar para casa!")
else:
  if estado == 3:
    print("Parado! Está cercado pelo Esquadrão De Segurança para Evitar o Paradoxo do Tempo. O que quer que você diga pode ou já foi usado contra você no Tribunal do Futuro.")
    print("Talvez não foi uma boa ideia ajudar o Ford…")
  print("Oh, não! O Ford vai ter que achar outro jeito de voltar para casa.")