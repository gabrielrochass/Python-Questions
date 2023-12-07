#rumo as oitavas
#rumo as oitavas
# vitoria += 1
# perdeu += 0
# empate += 1

#input
#nome1 = input()
#resutado1_1 = input()
#resutado2_1 = input()

#nome2 = input()
#resutado1_2 = input()
#resutado2_2 = input()

#nome3 = input()
#resutado1_3 = input()
#resutado2_3 = input()

#output
#print(f'Parabéns aos países {nome1} e {nome2}, vocês estão classificados para as oitavas de finais!!!'')

#rumo as oitavas
# vitoria += 1
# perdeu += 0
# empate += 1

#input
#nome1 = input()
#resutado1_1 = input()
#resutado2_1 = input()

#nome2 = input()
#resutado1_2 = input()
#resutado2_2 = input()

#nome3 = input()
#resutado1_3 = input()
#resutado2_3 = input()

#output
#print(f'Parabéns aos países {nome1} e {nome2}, vocês estão classificados para as oitavas de finais!!!'')

#inputs:
nome1 = input()
resultado1_jogo1 = input()
resultado2_jogo1 = input()
soma1 = 0

nome2 = input()
resultado1_jogo2 = input()
resultado2_jogo2 = input()
soma2 = 0

nome3 = input()
resultado1_jogo3 = input()
resultado2_jogo3 = input()
soma3 = 0

#bloco1
if resultado1_jogo1 == 'Ganhou':
  soma1 += 3
elif resultado1_jogo1 == 'Empatou':
  soma1 += 1

if resultado2_jogo1 == 'Ganhou':
  soma1 += 3
elif resultado2_jogo1 == 'Empatou':
  soma1 += 1
  
#bloco2
if resultado1_jogo2 == 'Ganhou':
  soma2 += 3
elif resultado1_jogo2 == 'Empatou':
  soma2 += 1
 
if resultado2_jogo2 == 'Ganhou':
  soma2 += 3
elif resultado2_jogo2 == 'Empatou':
  soma2 += 1
  
#bloco3
if resultado1_jogo3 == 'Ganhou':
  soma3 += 3
elif resultado1_jogo3 == 'Empatou':
  soma3 += 1

if resultado2_jogo3 == 'Ganhou':
  soma3 += 3
elif resultado2_jogo3 == 'Empatou':
  soma3 += 1
  

#calculo
if soma1 >= soma2 and soma2 > soma3:
  print(f'Parabéns aos países {nome1} e {nome2}, vocês estão classificados para as oitavas de finais!!!')
elif soma1 >= soma3 and soma3 > soma2:
  print(f'Parabéns aos países {nome1} e {nome3}, vocês estão classificados para as oitavas de finais!!!')
elif soma2 >= soma1 and soma1 > soma3:
  print(f'Parabéns aos países {nome1} e {nome2}, vocês estão classificados para as oitavas de finais!!!')
elif soma2 >= soma3 and soma3 > soma1:
  print(f'Parabéns aos países {nome2} e {nome3}, vocês estão classificados para as oitavas de finais!!!')
elif soma3 >= soma1 and soma1 > soma2:
  print(f'Parabéns aos países {nome1} e {nome3}, vocês estão classificados para as oitavas de finais!!!')
elif soma3 >= soma2 and soma2 > soma1:
  print(f'Parabéns aos países {nome2} e {nome3}, vocês estão classificados para as oitavas de finais!!!')
