objeto_procurado = input()
lista_itens = input()
lista_itens = lista_itens.split(', ')
# print(lista_itens)
# print(len(lista_itens))
itens_repetidos = []
coeficiente_erro = float()
qt_item_mais_repetido = 0
itens_diferentes = []
nao_repetidos = []
itens_iguais_print = []

for i in lista_itens:
  if i not in nao_repetidos:
    nao_repetidos.append(i)
  else:
    itens_repetidos.append(i)
    
for k in itens_repetidos:
  if k not in itens_diferentes:
    itens_diferentes.append(k)
    print(f'Após análises, percebi que {str(k)} foi coletado mais de uma vez...')

  else:
    itens_iguais_print.append(k)

itens_repetidos = []
for i in range(len(lista_itens)):
  qt_itens_repetidos = 0
  if lista_itens[i] not in itens_repetidos:
    for j in range(i+1, len(lista_itens)):
      if lista_itens[i] == lista_itens[j]:
        qt_itens_repetidos+=1
        itens_repetidos.append(lista_itens[i])
        
      if qt_item_mais_repetido <= qt_itens_repetidos:
        qt_item_mais_repetido = qt_itens_repetidos
        


if len(itens_repetidos) > 0:
  coeficiente_erro = (len(lista_itens)) / (qt_item_mais_repetido+1)
  print('Certo, o coeficiente de erros de viagens interdimensionais é {:.2f}'.format(coeficiente_erro))


if objeto_procurado in lista_itens and (objeto_procurado not in itens_repetidos): 
  print(f'Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!')
else:  
  print(f'Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...')
  
print('(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)')
print('O walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"')
print('(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)')




