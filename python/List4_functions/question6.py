def ascii(nome):
  c = 0
  for i in nome:
    c += ord(i)
  return c


def alocar_nome(celas, posicao, nome, qt_celas): # procurar a posicao livre e aloca prisioneiro

  if celas[posicao] == " ":
    celas[posicao] = nome
  else:
    while celas[posicao] != " ":
      posicao = (posicao + 1) % qt_celas
    celas[posicao] = nome

msg = input().split(" ")
qt_celas, qt_ordens = int(msg[0]), int(msg[1])
celas = [" "] * qt_celas
qt_nomes = 0

for i in range(0, qt_ordens):
  ordem = input().split(" ")
  comando = ordem[0]
  nome = ordem[1]
  codigoPrisioneiro = ascii(nome)
  posicao = codigoPrisioneiro % qt_celas

  if comando == "ADICIONAR":
    if qt_nomes == qt_celas:
      print("CHEIO")
    else:
      # aloca o prisioneiro e incrementa o contador
      alocar_nome(celas, posicao, nome, qt_celas)
      qt_nomes += 1
  elif comando == "REMOVER":
    if celas[posicao] == nome:
      # remove o prisioneiro e decrementa o contador
      celas[posicao] = " "
      qt_nomes -= 1
    else:
      if nome not in celas:
        print("NAO EXISTE")
      else:
        # remove o prisioneiro e decrementa o contador
        posicao = celas.index(nome)
        celas[posicao] = " "
        qt_nomes -= 1
        
# imprime os prisioneiros em ordem
list_nomes = []
for i in range(len(celas)):
  if celas[i] != " ":
    list_nomes.append(celas[i])
print(*list_nomes, sep=" ")