# consertar o portal
# exterminar criaturas desconhecidas
# restabelecer a energia
# encher os pneus do carro

# para consertar o portal:
# 1 - paginaPortal
# 2 - lanterna
# 3 - bobina
# 4 - martelo

# para exterminar as criaturas:
# 1 = paginaCriaturas
# 2 = lanterna
# 3 = espada

# para restabelcer energia:
# 1 = paginaEnergia
# 2 = lanterna
# 3 = fios
# 4 = martelo
  
# para encher os pneus:
# 1 = paginaPneus
# 2 = lanterna
# 3 = compressor

mat_portal = ['lanterna', 'paginaPortal', 'bobina', 'martelo']
mat_criaturas = ['lanterna', 'paginaCriaturas', 'espada']
mat_energia = ['lanterna', 'paginaEnergia', 'fios', 'martelo']
mat_pneus = ['lanterna', 'paginaPneus', 'compressor']

nomes = input().split(' ')
end = False
done_challenge1 = False
done_challenge2 = False
done_challenge3 = False
done_challenge4 = False
list_names = []
list_materiais = []

#cria uma lista pra cada nome, todos inicialmente com lanterna
for i in range(len(nomes)):
    list_materiais.append(['lanterna'])


#recebe os inputs
while not end: 
  acao = input().split(' ')
  if acao[0] not in nomes and (acao != ['END']):
      print(f'{acao[0]} não faz parte da equipe!')

  if acao == ['END']:
      end = True

  elif 'achou' in acao: #separa os itens no inventário de cada nome
      if acao[-1] not in list_materiais[nomes.index(acao[0])]:
          list_materiais[nomes.index(acao[0])].append(acao[-1])
      else:
        print(f'{acao[-1]} já encontrado por {acao[0]}.')

      if len(list_materiais[nomes.index(acao[0])]) <= 4:
          print(f'{acao[0]} coletou {acao[-1]}!!')
      else:
          print(f'{acao[0]} está com o máximo de itens! {acao[-1]} foi descartado.') 
  
  elif 'realizou' in acao:
      list_materiais[nomes.index(acao[0])] = ['lanterna']
      if acao[0] not in nomes: 
          print(f'{acao[0]} não faz parte da equipe!')
      
      if acao[-1] == 'portal':
          done_challenge1 = True
          print(f'{acao[0]} conseguiu consertar o portal!!!')
          
      elif acao[-1] == 'criaturas':
          done_challenge2 = True
          print(f'{acao[0]} conseguiu exterminar todas as criaturas!!!')           
         
      elif acao[-1] == 'energia':
          done_challenge3 = True
          print(f'{acao[0]} conseguiu restabelecer a energia do local. Ufa!!!')
         
      elif acao[-1] == 'carro':
          done_challenge4 = True
          print(f'{acao[0]} conseguiu consertar o carro!!! Entrem todos!')
          
      if 'perde' in acao:
        if 'lanterna' in list_materiais[nomes.index(acao[0])]:
          list_materiais[nomes.index(acao[0])].remove('lanterna')
      
         
  elif 'desistiu' in acao:
      if acao[0] not in nomes: 
        print(f'{acao[0]} não faz parte da equipe!')
      else:
        print(f'{acao[0]} abandonou a equipe! Não é porque somos menos que seremos mais fracos!!')


      if 'paginaPortal' in list_materiais[nomes.index(acao[0])] and 'lanterna' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['lanterna', 'paginaPortal']

      elif 'paginaPortal' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['paginaPortal']

      elif 'paginaCriaturas' in list_materiais[nomes.index(acao[0])] and 'lanterna' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['lanterna', 'paginaCriaturas']

      elif 'paginaCriaturas' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['paginaCriaturas']

      elif 'paginaEnergia' in list_materiais[nomes.index(acao[0])] and 'lanterna' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['lanterna', 'paginaEnergia']

      elif 'paginaEnergia' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['paginaEnergia']

      elif 'paginaPneus' in list_materiais[nomes.index(acao[0])] and 'lanterna' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['lanterna', 'paginaPneus']

      elif 'paginaPneus' in list_materiais[nomes.index(acao[0])]:
        list_materiais[nomes.index(acao[0])] = ['paginaPneus']

      else:
        if 'lanterna' in list_materiais[nomes.index(acao[0])]:
          list_materiais[nomes.index(acao[0])] = ['lanterna']

  

#comparar inventários finais com inventario necessário para realizar desafio
for i in range(len(list_materiais)):
  if len(list_materiais) >= 4:
#     mat_portal = ['lanterna', 'paginaPortal', 'bobina', 'martelo']
# mat_criaturas = ['lanterna', 'paginaCriaturas', 'espada']
# mat_energia = ['lanterna', 'paginaEnergia', 'fios', 'martelo']
# mat_pneus = ['lanterna', 'paginaPneus', 'compressor']
    if 'lanterna' in list_materiais[i] and 'paginaPortal' in list_materiais[i] and 'bobina' in list_materiais[i] and ' martelo' in list_materiais[i]:
      if done_challenge1 == False:
        done_challenge1 = True
        print(f'{nomes[i]} conseguiu consertar o portal!!!')
        
        
    elif 'lanterna' in list_materiais[i] and 'paginaCriaturas' in list_materiais[i] and 'espada' in list_materiais[i]:
      if done_challenge2 == False:
        done_challenge2 = True
        print(f'{nomes[i]} conseguiu exterminar todas as criaturas!!!')
        
    elif 'lanterna' in list_materiais[i] and 'paginaEnergia' in list_materiais[i] and 'fios' in list_materiais[i] and 'martelo' in list_materiais[i]:
      if done_challenge3 == False:
        done_challenge3 = True
        print(f'{nomes[i]} conseguiu restabelecer a energia do local. Ufa!!!')
    
    elif 'lanterna' in list_materiais[i] and 'paginaPneus' in list_materiais[i] and 'compressor' in list_materiais[i]:
      if done_challenge4 == False:
        done_challenge4 = True
        print(f'{nomes[i]} conseguiu consertar o carro!!! Entrem todos!')
    
    else:
      if done_challenge1 == False and done_challenge2 == False and done_challenge3 == False and done_challenge4 == False:
        print(f'{nomes[i]} não possui os itens necessários para fazer essa tarefa! Colete mais itens e tente novamente.')



if done_challenge1 == True and done_challenge2 == True and done_challenge3 == True and done_challenge4 == True:
  print('OBA! Stanford Pines conseguiu retornar à sua dimensão!!!')
  
elif done_challenge1 == False and done_challenge2 == True and done_challenge3 == True and done_challenge4 == True:
  print('Apenas o portal... Que pena! Stanford Pines preso para sempre??')
  
elif done_challenge1 == False and done_challenge2 == False and done_challenge3 == False and done_challenge4 == False:
  print('Nenhum avanço! Que fracasso, o Stanford ficará preso para sempre.')

else:
  print('Quase lá...')
  
print('(Você retorna ao banheiro do CIn, mas não se lembra do ocorrido. Vê um walkie-talkie na sua mão e decide voltar ao grad com ele, mas acaba esquecendo lá...)')
