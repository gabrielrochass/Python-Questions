#está chegando a final
#simular a final



# 0 < forca_ataque < 30
# 0 < consistencia_ataque < 30
#0 < folego < 5
# 1 < sorte < 2]
# 0 < canseira < 1

#Fator canseira: 1 - ( (5 - Fôlego)/10)

#2 tempos e 4 turnos
#um ataca, outro defende

#1 turno:
#A ataca x B defende

#2 turno:
#B ataca x A defende

#3 turno:
#B ataca x A defende

#4 turno:
#A ataca x B defende

#compara força_ataque - consistencia_defesa
# if forca_ataque >= consistencia defesa
# gola += 1

#folego
#fato canseira - diminui características

#turno 1: não há decrescimo das caracteristicas
#turno 2: caracteristicas decrescem com  (Valor da característica) * (Fator canseira)

# só força_ataque e consistencia_defesa saõ afetadas pela canseira

#cada turno:
#1: atribuição cansaço
#2: atribuição sorte
#3: comparação das características em seu valor atual

#inputs:
time1 = input()
forca_ataque1 = int(input())
consistencia_defesa1 = int(input())
folego1 = float(input())

time2 = input()
forca_ataque2 = int(input())
consistencia_defesa2 = int(input())
folego2 = float(input())

sorte1 = int(input())
sorte2 = int(input())
sorte3 = int(input())
sorte4 = int(input())

gol1 = 0
gol2 = 0


# 0 < canseira < 1

canseira1 = 1 - ((5 - folego1)/10)
canseira2 = 1 - ((5 - folego2)/10)

decrescimo1_defesa = consistencia_defesa1
decrescimo1_ataque = forca_ataque1

decrescimo2_defesa = consistencia_defesa2
decrescimo2_ataque = forca_ataque2


print('Início de jogo!')

#1 tempo
#turno 1:
#não há decrescimo das características
#A ataca
print('1° tempo:')
print(f'{time1} [{gol1}-{gol2}] {time2}')
print(f'O time {time1} vem pressionando.')
#atribução da sorte:
if sorte1 == 1:
  decrescimo1_ataque += 2
elif sorte1 == 2:
  decrescimo2_defesa += 2

#comp das carac

if decrescimo1_ataque >= decrescimo2_defesa:
  print(f'GOOOOOOOOOOOOLLLLLL DO TIME {time1}!!!')
  gol1 +=1
else: 
  print(f'O ataque é interrompido! Ótima defesa do time {time2}')

if sorte1 == 1:
  decrescimo1_ataque -= 2
elif sorte1 == 2:
  decrescimo2_defesa -= 2

##2 turno
#B ataca
print(f'O time {time2} vem pressionando.')

decrescimo1_defesa *= canseira1
decrescimo1_ataque *= canseira1

decrescimo2_ataque *= canseira2
decrescimo2_defesa *= canseira2

#atribuição da sorte:
if sorte2 == 1:
  decrescimo2_ataque += 2
elif sorte2 == 2:
  decrescimo1_defesa += 2

#folego1 -= canseira1
#folego2 -= canseira2

# print(f'{time1}: {decrescimo1_ataque} {decrescimo1_defesa} {consistencia_defesa1} {canseira1}')
# print(f'{time2}: {decrescimo2_ataque} {decrescimo2_defesa} {forca_ataque2} {canseira2}')

#comparação das carac
if (decrescimo2_ataque) >= (decrescimo1_defesa):
    print(f'GOOOOOOOOOOOOLLLLLL DO TIME {time2}!!!')
    gol2 +=1
else: 
    print(f'O ataque é interrompido! Ótima defesa do time {time1}')

if sorte2 == 1:
  decrescimo2_ataque -= 2
elif sorte2 == 2:
  decrescimo1_defesa -= 2

##2 tempo:
#1 turno: NÃO TA DEFENDENDO
#b ataca
print('2° tempo:')
print(f'{time1} [{gol1}-{gol2}] {time2}')
print(f'O time {time2} vem pressionando.')

#atribuição da canseira:
# canseira1 = 1 - ((5 - folego1)/10)
# canseira2 = 1 - ((5 - folego2)/10)


decrescimo1_defesa *= canseira1
decrescimo1_ataque *= canseira1

decrescimo2_ataque *= canseira2
decrescimo2_defesa *= canseira2

#atribuição da sorte:
if sorte3 == 1:
  decrescimo2_ataque += 2
elif sorte3 == 2:
  decrescimo1_defesa += 2

# print(f'{time1}: {decrescimo1_ataque} {decrescimo1_defesa} {consistencia_defesa1} {canseira1}')
# print(f'{time2}: {decrescimo2_ataque} {decrescimo2_defesa}')

# folego1 -= canseira1
# folego2 -= canseira2

#comparação das caracteristicas:

if (decrescimo2_ataque) >= (decrescimo1_defesa):
  print(f'GOOOOOOOOOOOOLLLLLL DO TIME {time2}!!!')
  gol2 +=1
else: 
  print(f'O ataque é interrompido! Ótima defesa do time {time1}')
  
if sorte3 == 1:
  decrescimo2_ataque -= 2
elif sorte3 == 2:
  decrescimo1_defesa -= 2

##2 turno do 2 tempo: !!!!!!
#A ataca
print(f'O time {time1} vem pressionando.')

#atribuição da canseira
canseira1 = 1 - ((5 - folego1)/10)
canseira2 = 1 - ((5 - folego2)/10)

decrescimo1_ataque *= canseira1
decrescimo1_defesa *= canseira1
decrescimo2_defesa *= canseira2
decrescimo2_ataque *= canseira2

#folego1 -= canseira1
#folego2 -= canseira2

#atribuição da sorte:
if sorte4 == 1:
  decrescimo1_ataque += 2
elif sorte4 == 2:
  decrescimo2_defesa += 2

#comp das carac
if (decrescimo1_ataque) >= (decrescimo2_defesa):
  print(f'GOOOOOOOOOOOOLLLLLL DO TIME {time1}!!!')
  gol1 +=1
else: 
  print(f'O ataque é interrompido! Ótima defesa do time {time2}')

if sorte4 == 1:
  decrescimo1_ataque -= 2
elif sorte4 == 2:
  decrescimo2_defesa -= 2


#placar final;
print(f'{time1} [{gol1}-{gol2}] {time2}')

##resultado final e print final:
if gol1 == gol2:
  print(f'Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!')
elif gol1 > gol2:
  print(f'ACABOOOOU!! O TIME {time1} É O CAMPEÃO!!!')
elif gol2 > gol1:
  print(f'Fim de jogo! O time {time2} é campeão.')

