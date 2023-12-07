# qual dos petcinhos tá mais propenso a causar confusão
#verificar estado de cada um

#calmo/ agitado
# sempre tem um amigo

# pets propensos a bagunçar:
# aqueles com só um amigo pets
#agitados e amigos >= 7

#min de 2 pets na creche


#cria listas:
list_nomes = []
list_estado = []
list_amigos = []
list_qt_amigos = []
qt_agitado = 0
qt_calmo = 0
list_nomes_final = []

# recebe o numero de pets a serem cuidados:
qt_pets = int(input())

#organiza informação
info_organizada = {'nome': tuple(),'estado': tuple(), 'amigos': tuple()}

#pega as informações:
for i in range(qt_pets):
  informacoes = input().split(', ')
  info_organizada['nome'] = list_nomes.append(informacoes[0])
  info_organizada['estado'] = list_estado.append(informacoes[1])
  info_organizada['amigos'] = list_amigos.append(informacoes[2:])
  info_organizada['quantidade de amigos'] = list_qt_amigos.append(len(informacoes[2:]))

# print(list_nomes)
# print(list_amigos)
# print(list_estado)
# print(list_qt_amigos)

#verifica qauntidade de agitados e calmos
for n in range(len(list_estado)):
  if list_estado[n] == 'agitado' or (list_estado[n] == 'calmo' and list_qt_amigos[n] == 1):
    # x = list_estado.index(list_estado[n])
    # print(x)
    # print(list_qt_amigos[x])
    
    if list_qt_amigos[n] <= 3:
      list_nomes_final.append(list_nomes[n])
      # print(list_nomes_final)
      # qt_agitado += 1
    
    # list_estado.remove(list_estado[n])
    # # print(list_nomes)
    # list_nomes.remove(list_nomes[x])
    # list_qt_amigos.remove(list_qt_amigos[x])
    # # print(list_nomes)
    # # print(list_qt_amigos)
    
  # else:
  #   qt_calmo += 1

# print(list_estado)
# print(list_nomes_final)
#verifica periculosidade
if len(list_nomes_final)==0:
  print('Todos estão se divertindo tranquilamente! Os queridos cuidadores podem relaxar!')


elif len(list_nomes_final)==1:
  w = ''.join(list_nomes_final)
  print(f'Apenas {w} está querendo bagunçar, deem carinho e atenção imediatamente!')
  
else:
  # print(list_nomes_final)
  ultimo = list_nomes_final.pop(-1)
  # ultdog = list_nomes_final[-1]
  # lnfr = list_nomes_final.remove(list_nomes_final[-1])
  y = ', '.join(list_nomes_final)
  print(f'Vai ser um trabalho difícil, mas {y} e {ultimo} podem acabar atrapalhando os alunos do CIn!')
  
  

#tuple([])
# baralho.keys() -> retorna chaves em formato de lista
# baralho.values() -> retorna valores de cada chave em forma de lista
  


