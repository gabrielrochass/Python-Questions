# votação
# melhor lugar = maior total de pontos
# pior lugar = menor total de pontos

#input
total_lugares = int(input()) #total de lugares sugeridos
melhor_nota = 0
pior_nota = -1
total_pontos = 0
melhor_lugar = ''
nota_n = 0
empate = bool()
lugares_empatados = ''
#lugares:
for i in range(total_lugares):
  nome_lugar = input() #nome do lugar sugerido
 #número indefinido de notas
  total_pontos = 0
  nota = 0
  while nota >= 0: #para quando uma das notas tiver valor < 0
    nota = int(input())
    if nota >= 0:
      total_pontos += nota
    
  if total_pontos > melhor_nota:
    melhor_nota = total_pontos
    melhor_lugar = nome_lugar
    empate = False
  elif melhor_nota == total_pontos:
    empate = True
    melhor_lugar = f'{melhor_lugar}, {nome_lugar}'
    
  
  if pior_nota == -1 or pior_nota > total_pontos:
    pior_nota = total_pontos
    pior_lugar = nome_lugar

  

if not empate:
  print(f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {melhor_nota} vs {pior_nota}')
else: 
  print(f'{melhor_lugar}\nTantas opções')

  
  #output:
  #se n ocorrer empate para melhor lugar
  