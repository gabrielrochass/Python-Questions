# registrar informações de cada animal
# dado um mês -> retornar nome, espécie, aniversariantes

list_nomes = []
list_especies = []
list_aniv = []
list_mes = []
list_nomes_sorted = []
list_mes_sorted = []
list_especies_sorted = []

#organiza informações:
# def organizarInformacoes(info):
info_organizada = {'nome': list, 'espécie': list, 'aniversário': list}


#recebe a quantidade de animais cadastrados:
qt_animais = int(input())

#recebe n linhas com nome, espécie e aniversárion e organiza em listas
for i in range(qt_animais):
  informacoes = input().split(' ') 
  # print(informacoes)
  list_nomes.append(informacoes[0])
  list_especies.append(informacoes[1])
  list_aniv.append(informacoes[2])
  
# print(list_nomes)
# print(list_especies)
# print(list_aniv)

#pega o mês de aniversário:
for k in range(len(list_aniv)):
  list_mes.append(int(list_aniv[k][3] + list_aniv[k][4]))
# print(sorted(list_mes))
# print(list_mes.index(3))


# print(list_nomes)
# print(list_mes)
# print(list_especies)


#ordena listas
list_nomes_sorted = sorted(list_nomes)
# print(list_nomes_sorted)

for k in list_nomes_sorted:
  y = list_nomes.index(k)
  list_mes_sorted.append(list_mes[y])
  list_especies_sorted.append(list_especies[y])
# print(list_mes_sorted)
# print(list_especies_sorted)
  


for j in range(len(list_nomes)):
  info_organizada['nome'] = list_nomes_sorted
  info_organizada['espécie'] = list_especies_sorted
  info_organizada['aniversário'] = list_mes_sorted
# print(str(info_organizada))


  
#recebe o mês analisado:
mes_analisado = int(input())

#compara mes analisado com os aniversários
if mes_analisado in list_mes_sorted:
  print('E os donos da festa do mes sao:')
  for c in range(list_mes_sorted.count(mes_analisado)):
    x = list_mes_sorted.index(mes_analisado)
    # print(x)
    print(f'{list_nomes_sorted[x]} - {list_especies_sorted[x]}')
    info_organizada['aniversário'].remove(list_mes_sorted[x])
    info_organizada['nome'].remove(list_nomes_sorted[x])
    info_organizada['espécie'].remove(list_especies_sorted[x])

else:
  print('Sem festa esse mes. :(')
