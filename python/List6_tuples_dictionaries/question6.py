# definir o caminho viável da fofoca até o gato certo
# ou informar q n há como repassar a fofoca

# mau relacionamento: n repassar
# bom relacionamento: sem intermed
# sem relacionamento: passa p outro gato q tem um bom relacionamento até o gato destino

# se n tem como chegar até o destino -> sem solução

# dicionario de lista ou dicionario de dicionario
# recursao

#organizando
informacoes = {}

# recebe o numero de residentes:
qt_gatos = int(input())

#recebe informacoes dos qt_gatos
for i in range(qt_gatos):
  nome = input()
  amigos = input().split(' ')
  inimigos = input().split(' ')
  
  informacoes[nome] = {'amigos': (amigos), 'inimigos': (inimigos)}
  # print(informacoes)

# recebe nome do gato 
recepcao = input()
destino = input()

def verifica_malRelacionamento(recepcao, destino):
  if destino in informacoes[recepcao]['inimigos']:
    print(f'Eu não falo com {destino}! Mas fico feliz por ter sido edificado com essa fofoca')

def verifica_bomRelacionamento(recepcao, destino):
  if destino in informacoes[recepcao]['amigos']:
    return print(f'Fofoca? Aceito. Vou contar agora mesmo, miau miau')

#verifica caminho  
def achar_caminho(dic, recepcao, destino, caminho=[]):
  # adiciona a recepcao ao caminho
  caminho = caminho + [recepcao]
  
  # verifica se recepcao = destino -> caso base
  if recepcao == destino:
    return caminho
  
  # verifica se a chave atual não tá no dicionário
  if recepcao not in dic:
    return None
  
  # verifica todos os amigos do 2 parametro
  for k in dic[recepcao]['amigos']:
    if k not in caminho:
      novo_caminho = achar_caminho(dic, k, destino, caminho)
      if novo_caminho:
        return novo_caminho
  
  # retorna None se não houver caminho
  return None

caminho = achar_caminho(informacoes, recepcao, destino)
print_unico = False

if destino in informacoes[recepcao]['inimigos'] and print_unico == False:
  print(f'Eu não falo com {destino}! Mas fico feliz por ter sido edificado com essa fofoca')
  print_unico = True

elif destino in informacoes[recepcao]['amigos'] and print_unico == False:
  print(f'Fofoca? Aceito. Vou contar agora mesmo, miau miau')
  print_unico = True

if caminho != None and print_unico == False:
  print(f'Finalmente recebi a fofoca! Ela começou em {caminho[0]}', end = ' ')
  for g in range(len(caminho)-2):
    print(f'que contou a {caminho[g+1]}', end = ' ')
    if (g+1) == len(caminho) - 2:
      print(f'e chegou em mim', end = '')

else:
  if print_unico == False:
    print('Infelizmente não tem como fofocar, melhor procurar outro gato!')
# print(caminho)


