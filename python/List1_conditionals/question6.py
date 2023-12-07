#exercico

#banco de dados com a colocação dos times na última copa

#tipos de consultas:

# com base critério geral: vit + 3; emp + 1; derr + 0
# por ordem alfabética

#inputs:

#ano da copa

#nome_selecao1
#vitorias_time1
#empates_time1

#nome_selecao2
#vitorias_time2
#empates_time2

#nome_selecao3
#vitorias_time3
#empates_time3

#tipo_consulta: lexicográfica (alfabética) ou critério geral

#output

#if consulta por critério geral
#print(f'a classificação na copa de {ano} foi: ')
#1 - time a - pontos
#2 - time b - pontos
#3 time c - pontos


#if consulta por ordem lexicográfica
#print(f'os times por ordem lexicográfica da copa de {ano} são: ')
#1 - time a - pontos
#2 - time b - pontos
#3 time c - pontos

#inputs:
ano = int(input())
nome_selecao1 = input()
vitorias_time1 = int(input())
empates_time1 = int(input())
nome_selecao2 = input()
vitorias_time2 = int(input())
empates_time2 = int(input())
nome_selecao3 = input()
vitorias_time3 = int(input())
empates_time3 = int(input())
tipo_consulta = input()

#calculo da pontuação
pontos_vitoria1 = vitorias_time1 * 3
pontos_empate1 = empates_time1 * 1
total1 = pontos_empate1 + pontos_vitoria1

pontos_vitoria2 = vitorias_time2 * 3
pontos_empate2 = empates_time2 * 1
total2 = pontos_empate2 + pontos_vitoria2

pontos_vitoria3 = vitorias_time3 * 3
pontos_empate3 = empates_time3 * 1
total3 = pontos_empate3 + pontos_vitoria3

#classificação critério geral
if (tipo_consulta == 'Critério Geral'):

  if (total1 > total2 and total2 > total3):
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao1} - {total1}\n{nome_selecao2} - {total2}\n{nome_selecao3} - {total3}')

  elif (total1 > total3 and total3 > total2):
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao1} - {total1}\n{nome_selecao3} - {total3}\n{nome_selecao2} - {total2}')

  elif (total2 > total1 and total1 > total3):
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao2} - {total2}\n{nome_selecao1} - {total1}\n{nome_selecao3} - {total3}')

  elif (total2 > total3 and total3 > total1):
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao2} - {total2}\n{nome_selecao3} - {total3}\n{nome_selecao1} - {total1}')

  elif (total3 > total1 and total1 > total2):
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao3} - {total3}\n{nome_selecao1} - {total1}\n{nome_selecao2} - {total2}')

  elif (total3 > total2 and total2 > total1):
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao3} - {total3}\n{nome_selecao2} - {total2}\n{nome_selecao1} - {total1}')
  else:
    print(f'A classificação na copa de {ano} foi:\n{nome_selecao3} - {total3}\n{nome_selecao2} - {total2}\n{nome_selecao1} - {total1}')

#classificação ordem lexicográfica
if (tipo_consulta == 'Ordem Lexicográfica'): 
  if (nome_selecao1 < nome_selecao2 and nome_selecao2 < nome_selecao3):
    print(f'O times por ordem Lexicográfica da copa de {ano} são:\n{nome_selecao1} - {total1}\n{nome_selecao2} - {total2}\n{nome_selecao3} - {total3}')

  elif (nome_selecao1 < nome_selecao3 and nome_selecao3 < nome_selecao2):
    print(f'O times por ordem Lexicográfica da copa de {ano} são:\n{nome_selecao1} - {total1}\n{nome_selecao3} - {total3}\n{nome_selecao2} - {total2}')

  elif (nome_selecao2 < nome_selecao1 and nome_selecao1 < nome_selecao3):
    print(f'O times por ordem Lexicográfica da copa de {ano} são:\n{nome_selecao2} - {total2}\n{nome_selecao1} - {total1}\n{nome_selecao3} - {total3}')

  elif (nome_selecao2 < nome_selecao3 and nome_selecao3 < nome_selecao1):
    print(f'O times por ordem Lexicográfica da copa de {ano} são:\n{nome_selecao2} - {total2}\n{nome_selecao3} - {total3}\n{nome_selecao1} - {total1}')

  elif (nome_selecao3 < nome_selecao1 and nome_selecao1 < nome_selecao2):
    print(f'O times por ordem Lexicográfica da copa de {ano} são:\n{nome_selecao3} - {total3}\n{nome_selecao1} - {total1}\n{nome_selecao2} - {total2}')

  elif (nome_selecao3 < nome_selecao2 and nome_selecao2 < nome_selecao1):
    print(f'O times por ordem Lexicográfica da copa de {ano} são:\n{nome_selecao3} - {total3}\n{nome_selecao2} - {total2}\n{nome_selecao1} - {total1}')
  
