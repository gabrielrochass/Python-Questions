# analisar quais pets podem ficar juntos
# oq precisa mudar na casa dele

# organizar com dicionários
import itertools

# potenciais escolhas = gato, cachorro, peixe e hamster
animais = ('cachorro', 'gato', 'hamster', 'peixe')
inimigos = {'cachorro': ('gato'), 'gato': ('cachorro', 'hamster', 'peixe'), 'hamster': ('cachorro', 'gato'), 'peixe': ('gato')}
necessidades = {'cachorro': ['coleira', 'ração', 'ursinho de pelúcia'], 'gato': ['bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo'], 'hamster': ['ração', 'roda para hamster', 'serragem'], 'peixe': ['aquário', 'filtro', 'ração']}

# animais recem-nascidos nunca são inimigos
# animais da mesma espécie são amigos

# recebe os nomes para consulta
nomes_consultados = input().split(' e ')
# print(nomes_consultados)

#verifica se são recem-nascidos -> n tem inimigos
recem_nascidos = False
tem_inimigos = False
sn = input()

if sn == 'sim':
  recem_nascidos = True

#verifica se o animal ta na lista
fim = False
for i in nomes_consultados:
  if i not in animais:
    i_join = ''.join(i)
    print(f'Sérgio, o animal {i_join} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.')
    #outros outpus desconsiderados
    # break
    fim = True
    
# verifica se eh recem_nascidos
if fim == False:
  if recem_nascidos:
    fim = True
    print(f'Como os animais são recém nascidos, eles podem ser adotados juntos!\nSegue aqui as necessidades dos animais:')
    for i in range(len(nomes_consultados)):
      print(f'As necessidades do(a) {nomes_consultados[i]} são:')
      # print(necessidades['gato'])
      # print(nomes_consultados[i])
      # print(len(necessidades['gato']))
      for j in range(len(necessidades[nomes_consultados[i]])):
        print(f'- {necessidades[nomes_consultados[i]][j]};')
    print('Dito isso, vamos adotá-los!!!')
  
  else:
    for i in nomes_consultados:
      for j in nomes_consultados:
        if i != j:
          # print(f'({i}, {j})')
          if j in inimigos[i]:
            print(f'Sérgio, o(a) {i} tem o(a) {j} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos')
            tem_inimigos = True
            # print(f'Sérgio, o(a) {j} tem o(a) {i} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos')

if not tem_inimigos and fim == False:
  print('Segue aqui as necessidades dos animais:')
  for i in nomes_consultados:
    print(f'As necessidades do(a) {i} são:')
    for j in range(len(necessidades[i])):
      print(f'- {necessidades[i][j]};')
  print('Dito isso, vamos adotá-los!!!')
  
            
            
       
  
  
