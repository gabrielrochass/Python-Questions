#disputa de penaltis

#mais gols or não tem mais como virar
#contagem de gols de uma disputa de penaltis
#definir qual seleção passa
#admite empate 5x5

#inputs:

#nomes das seleções
#nome1
#nome2

#pelo menos 10 entradas de penaltis
#4 possibilidades: gol, errou, na trava e defendeu
#apenas a entrada 'gol' conta como gol

#entrada impar - nome1
#entrada par - nome 2

#penalti = input()

#gols_vencedor
#gols_perdedor
#numero_de_gols
#output

#2 possibilidades de saída
#com vencedor:
# print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase')

#empate:
#print(f'Ambas as seleções terminaram com {numero_de_gols} gols, mas o desempate vai ficar para outro dia.')

#inputs
nome1 = input()
nome2 = input()
penalti1 = input()
penalti2 = input()
penalti3 = input()
penalti4 = input()
penalti5 = input()
penalti6 = input()
total1 = int()
total2 = int()


#calculo
if penalti1 == 'Gol':
  total1 += 1
if penalti2 == 'Gol':
  total2 += 1
if penalti3 == 'Gol':
  total1 += 1
if penalti4 == 'Gol' :
  total2 += 1
if penalti5 == 'Gol': 
  total1 += 1

# a partir do penalti 6:

if penalti6 == 'Gol':
  total2 += 1

if abs(total1 - total2) == 3:
  if total2 > total1:
    print(f'{nome2} vence a disputa de pênaltis por {total2} a {total1} e avança de fase!')
  else:
    print(f'{nome1} vence a disputa de pênaltis por {total1} a {total2} e avança de fase!')
else:
  penalti7 = input()
  if (penalti7 == 'Gol'):
    total1 += 1
  if (total1 == 4 and total2 == 1) or (total1 == 1 and total2 == 3): 
    if total1 > total2:
      print(f'{nome1} vence a disputa de pênaltis por {total1} a {total2} e avança de fase!')
    else:
      print(f'{nome2} vence a disputa de pênaltis por {total2} a {total1} e avança de fase!')
  else:
    penalti8 = input()
    if penalti8 == 'Gol':
      total2 += 1
    if (total1 == 3 and total2 == 1) or (total1 == 2 and total2 == 4):
      if total2 > total1:
        print(f'{nome2} vence a disputa de pênaltis por {total2} a {total1} e avança de fase!')
      else:
        print(f'{nome1} vence a disputa de pênaltis por {total1} a {total2} e avança de fase!')
    else:
      penalti9 = input()
      if penalti9 == 'Gol':
        total1 += 1
      if (total1 == 4 and total2 == 2) or (total1 == 2 and total2 == 3):
        if total2 > total1:
          print(f'{nome2} vence a disputa de pênaltis por {total2} a {total1} e avança de fase!')
        else:
          print(f'{nome1} vence a disputa de pênaltis por {total1} a {total2} e avança de fase!')
      else:
        penalti10 = input()
        if penalti10 == 'Gol':
          total2 += 1
        if total2 > total1:
          print(f'{nome2} vence a disputa de pênaltis por {total2} a {total1} e avança de fase!')
        elif total1 > total2:
          print(f'{nome1} vence a disputa de pênaltis por {total1} a {total2} e avança de fase!')
        else:
          print(f'Ambas as seleções terminaram com {total2} gols, mas o desempate vai ficar para outro dia.')
