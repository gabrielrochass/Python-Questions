# indicar em qual dos três cadernos se encontra o conteúdo buscado
# receber nomes de determinada quantidade de registro
# armazenar no idário correspondente
# permitir que o usuário busque pelo nome do diário

# input

num = int(input())
lista_diarios = []

# lista_conteudos = []
for i in range(num):
  dupla = input().split(', ')
  lista_diarios.append(dupla)
num_informacoes = int(input())
for j in range(num_informacoes):
  conteudo_buscado = input()
  n = 0
  # lista_conteudos.append(conteudo_buscado)
  for k in lista_diarios:
    if conteudo_buscado  == k[0]:
      print(f'Informacoes sobre {conteudo_buscado} estao no Diario {k[1]}')
    else:
      n += 1
      
  if n == num:
    print(f'Nenhum dos diarios possui informacoes sobre {conteudo_buscado}')
      
      
# output


  
  
  