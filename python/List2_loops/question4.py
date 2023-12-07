'''
protetor
dinheiro

chovendo = não vai a praia

inicio:
- protetor = False
- 0 dinehiro
- sol = True

input

inúmeras entradas -> while
dinheiro = float(input())
protetor == 'passar protetor' = True
clima = input()
  if clima = sol = True
  else: n vai

fim == 'ir para a praia'

output

duas saídas

1 - se foi
2 - como chegou da praia

if clima == 'chuvoso'
print(Hoje não vai dar pra ir, chuvinha barrou)

if clima == 'ensolarado'
  print(Hoje tem sol e mar!)
  if protetor = False and dinheiro < 10:
    print(Você não chegou muito bem, chame um médico!)
  elif protetor = False and dinheiro >= 10:
    print(O novo camarão do CIn foi criado)
  elif protetor == True and dinehiro < 10:
    print(Só faltou uma aguinha de coco...)
  elif protetor = True and dinheiro >= 10:
    print(Aí sim! Hoje rendeu!)

'''
#inicio:

protetor = False
sol = True
fim = bool()
moeda = 0

#inputs:

while fim == False:
  entrada = input()
  if entrada == 'passar protetor':
    protetor = True
  # else:
  #   protetor = False
  
  if entrada == 'separar dinheiro':
    dinheiro = float(input())
    moeda += dinheiro
    # print(moeda)
    
  if entrada == 'choveu':
    sol = False

  if entrada == 'parou de chover':
    sol = True
  
  if entrada == 'ir para a praia':
    fim = True

if sol:
  print('Hoje tem sol e mar!')
  if (protetor == False) and (moeda < 10):
    print('Você não chegou muito bem, chame um médico!')
  if (protetor == False) and (moeda >= 10):
    print('O novo camarão do CIn foi criado')
  if (protetor == True) and (moeda) < 10:
    print('Só faltou uma aguinha de coco...')
  if (protetor == True) and (moeda >= 10):
    print('Aí sim! Hoje rendeu!')

if sol == False:
  print('Hoje não vai dar pra ir, chuvinha barrou')
    
  













