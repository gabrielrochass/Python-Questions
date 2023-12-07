#ordenando criaturas
#colocar craturas em ordem alfabética

#input
numero_criatura = int(input())
lista_criaturas = []
lista_final = []
k = ''
n = 0
idx = 0
for i in range(numero_criatura):
  nome_criaturas = input()
  lista_criaturas.append(nome_criaturas)
  # lista_criaturas.sort() 
  # como ordenar uma lista sem função sort:
  for i in range(len(lista_criaturas)):
    for j in range(i+1, len(lista_criaturas)):
      if lista_criaturas[i] > lista_criaturas[j]:
        lista_criaturas[i], lista_criaturas[j] = lista_criaturas[j], lista_criaturas[i]
  
  # for k in lista_criaturas:
  #   if lista_criaturas[] > lista_criaturas[+1]:
  #     lista_criaturas.append(k)
  #   else:
  #     lista_criaturas.insert()
      

#output
for n in lista_criaturas:
  if n not in lista_final:
    lista_final.append(n)
  
print(', '.join(lista_final))
# print(lista_criaturas)
# nova_lista = lista_criaturas.sort()
# print(nova_lista)
