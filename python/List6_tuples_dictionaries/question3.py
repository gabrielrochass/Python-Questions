# definir se um sujeiro canino foi comportado o suficente para entrar na creche

#nomes, raças, notas
#calcula a média de acordo com as notas - aprovação, reprovação,recuperação

# notas referentes a: atividade,obediência e socialização

# Em seguida ele mostrará o nome de cada um dos doguinhos aprovados, reprovados e em recuperação, 
#seguindo a ordem de inserção no cadastro juntos de sua respectiva raça e sua média.

#aprovado: media >= 5
#reprovação <= 2
#recuperação: else

#transforma em float
def trans_float(entrada):
  for j in range(len(entrada)):
    entrada[j] = float(entrada[j])
  return entrada
 
#calcula a media: 
def calcula_media(entrada):
  soma = 0
  for k in range(len(entrada)):
    soma += entrada[k]
  
  media = soma/3
  return media
  
#verifica situação
def ver_situ(entrada):
  if entrada >= 3:
    return 'Aprovado'
  elif entrada < 2:
    return 'Reprovado'
  else:
    return 'Em recuperação'
    
#organiza aprovados, reprovados e em recuperação
# def organiza_aprovados(dicio):
#   if info_organizada['situação'] == 'Aprovado':
#     list_aprovados.append(info_organizada['nome'])
#     list_aprovados.append(info_organizada['raça'])
#     list_aprovados.append(info_organizada['média'])
#     list_tds_aprovados.append(list_aprovados)

  return list_aprovados
  #,list_reprovados, list_rec
    

#recebe o número de cachorros
qt_dogs = int(input())

list_aprovados = []
list_reprovados = []
list_rec = []


#organiza info
info_organizada = {'nome': list(), 'raça': tuple(), 'notas': list(), 
'média': int, 'situação': str}

print_unico1 = False
print_unico2 = False
print_unico3 = False
# transforma as informacoes em lista
for i in range(qt_dogs):

  informacoes = input().split(', ')
  # print(informacoes)
  info_organizada['nome'] = informacoes[0]
  info_organizada['raça'] = informacoes[1]
  info_organizada['notas'] = informacoes[2:]
  trans_float(info_organizada['notas'])
  info_organizada['média'] = calcula_media(info_organizada['notas'])
  info_organizada['situação'] = ver_situ(info_organizada['média'])

  # print(organiza_aprovados(info_organizada))

  if info_organizada['situação'] == 'Aprovado':
    if print_unico1 == False:
      print('Estao aprovados e de parabens os seguintes coleguinhas:')
      print_unico1 = True
    print(f'{info_organizada["nome"]} - {info_organizada["raça"]} - media: {info_organizada["média"]:.2f}')
   
   
  elif info_organizada['situação'] == 'Reprovado':
    list_reprovados.append(info_organizada['nome'])
    list_reprovados.append(info_organizada['raça'])
    list_reprovados.append(info_organizada['média'])
    
    
  else:
    list_rec.append(info_organizada['nome'])
    list_rec.append(info_organizada['raça'])
    list_rec.append(info_organizada['média'])

if len(list_reprovados) > 0:    
  print('Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):')
  
  for i in range(len(list_reprovados)):
      if i == 0:
          i = 0
          print(f'{list_reprovados[i]} - {list_reprovados[i+1]} - media: {list_reprovados[i+2]:.2f}')
      elif i == 1:
          if (i + 2) >= len(list_reprovados):
              break
          i = 3
          print(f'{list_reprovados[i]} - {list_reprovados[i+1]} - media: {list_reprovados[i+2]:.2f}')
      elif i == 2:
          if (i + 2) >= len(list_reprovados):
              break
          i = 6
          if i >= len(list_reprovados):
              break
          print(f'{list_reprovados[i]} - {list_reprovados[i+1]} - media: {list_reprovados[i+2]:.2f}')
      elif i == 3:
          if (i + 2) >= len(list_reprovados):
              break
          i = 9
          if i >= len(list_reprovados):
              break
          print(f'{list_reprovados[i]} - {list_reprovados[i+1]} - media: {list_reprovados[i+2]:.2f}')
  
      elif i == 4:
          if (i + 2) >= len(list_reprovados):
              break
          i = 12
          if i >= len(list_reprovados):
              break
          print(f'{list_reprovados[i]} - {list_reprovados[i+1]} - media: {list_reprovados[i+2]:.2f}')
      elif i == 5:
          if (i + 2) >= len(list_reprovados):
              break
          i = 15
          if i >= len(list_reprovados):
              break
          print(f'{list_reprovados[i]} - {list_reprovados[i+1]} - media: {list_reprovados[i+2]:.2f}')
      
if len(list_rec) > 0:  
  print('Esses queridos terao uma nova chance e prometem melhorar:')
  for i in range(len(list_rec)):
      if i == 0:
          i = 0
          print(f'{list_rec[i]} - {list_rec[i+1]} - media: {list_rec[i+2]:.2f}')
      elif i == 1:
          if (i + 2) >= len(list_rec):
              break
          i = 3
          print(f'{list_rec[i]} - {list_rec[i+1]} - media: {list_rec[i+2]:.2f}')
      elif i == 2:
          if (i + 2) >= len(list_rec):
              break
          i = 6
          if i >= len(list_rec):
              break
          print(f'{list_rec[i]} - {list_rec[i+1]} - media: {list_rec[i+2]:.2f}')
      elif i == 3:
          if (i + 2) >= len(list_rec):
              break
          i = 9
          if i >= len(list_rec):
              break
          print(f'{list_rec[i]} - {list_rec[i+1]} - media: {list_rec[i+2]:.2f}')
  
      elif i == 4:
          if (i + 2) >= len(list_rec):
              break
          i = 12
          if i >= len(list_rec):
              break
          print(f'{list_rec[i]} - {list_rec[i+1]} - media: {list_rec[i+2]:.2f}')
      elif i == 5:
          if (i + 2) >= len(list_rec):
              break
          i = 15
          if i >= len(list_rec):
              break
          print(f'{list_rec[i]} - {list_rec[i+1]} - media: {list_rec[i+2]:.2f}')
          

    

    
  # print(info_organizada)
    
  # print(trans_float(info_organizada['notas']))
  # print(f'{calcula_media(info_organizada["notas"]):.2f}')
  # print(ver_situ(calcula_media(info_organizada['notas'])))
  # # print(info_organizada.items())
  # # print(info_organizada.values())

  
  

