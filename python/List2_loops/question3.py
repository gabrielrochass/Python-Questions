# x amigos em estados diferentes
# melhor roteiro para visitar todos

#jogo para descobrir qual estado ir primeiro e quantos dias vai ficar

#ganha o estado que tiver mais vezes a letra sorteada em seu nome 
#quantidade de dias = quantidade de vezes que a letra se repete

#definir estado de preferencia

#input

letra_sorteada = input()
quantidade_amigos = int(input())
dias = 0
estado_preferencia = input()
maior = 0
maior_estado = ''

for i in range(quantidade_amigos):
  nome_amigo = input()
  estado = input()
  dias = 0
  for i in estado:
    if i == letra_sorteada:
      dias += 1
  if dias > maior:
    maior = dias
    maior_estado = estado

if maior_estado == estado_preferencia:
  print(f'UHUL!!! Victor vai começar por {estado_preferencia} que é o estado que ele queria e ficara la por {maior} dias.')
else:
  print(f'Eita!!! infelizmente, Victor terá que fazer uma viagem maior e começar pelo estado {maior_estado} e ficara la por {maior} dias.')
 

