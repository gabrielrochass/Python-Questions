
#quem roubou o artefato misterioso:
#investigar lista de frequentadores
#recebe entrada sem fim determinado -> while
#s.index[] +1
#lista[a], lista[b] = b, a => troca as posições dos elementos de uma lista
#input
fim = False
suspeitos = []
while not fim:
  entrada = input()
  if entrada == "novo suspeito - altissima periculosidade":
    novo_suspeito = input()
    suspeitos.insert(0, novo_suspeito)
    
  if entrada == "novo suspeito - pouco perigoso":
    novo_suspeito2 = input()
    suspeitos.append(novo_suspeito2)
    
  if entrada == "livre de suspeita, pode remover":
    novo_suspeito3 = input()
    suspeitos.remove(novo_suspeito3)
    
  if entrada == "sujeito mais perigoso do que pensavamos":
    indice_futuro = int(input())
    indice_tobeatualizado = int(input())
    suspeitos[indice_futuro],suspeitos[indice_tobeatualizado] = suspeitos[indice_tobeatualizado],suspeitos[indice_futuro]
    
  if entrada == "que estranho, esses dois meliantes… troque-os de lugar":
    nome1 = str(input())
    nome2 = str(input())
    if nome1 in suspeitos and nome2 in suspeitos:
      indice_nome1 = suspeitos.index(nome1)
      indice_nome2 = suspeitos. index(nome2)
      suspeitos[indice_nome1], suspeitos[indice_nome2] = suspeitos[indice_nome2], suspeitos[indice_nome1]
    
  if entrada == "essa posicao nao esta de acordo, ele nao e tao perigoso assim":
    nome3 = str(input())
    suspeitos.remove(nome3)
    suspeitos.append(nome3)
    # if nome3 in suspeitos:
    #   indice_nome3 = suspeitos.index(nome3)
    # suspeitos[indice_nome3], suspeitos[-1] = suspeitos[-1], suspeitos[indice_nome3]
    
  if entrada == "como a lista esta ficando?":
    print(' '.join(suspeitos)) 

  if entrada == "ja temos nossa lista de suspeitos":
    fim = True
print('O resultado final ficou assim:')
print(' '.join(suspeitos))
