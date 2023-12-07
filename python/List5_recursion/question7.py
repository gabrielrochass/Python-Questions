viloes = ["CHARADA","ARLEQUINA", "PINGUIM",
"JOKER", "ESPANTALHO", "DUASCARAS","REIDOSCONDIMENTOS"]

caca_palavras = []
qt_ij = int(input())
for i in range(qt_ij):
  caca_palavras.append(input().split())
  
#verifica vizinhos
def cacar(x, y, nome, index_letra):
  if x < 0 or x >= qt_ij or y < 0 or y >= qt_ij:
    return ""
  elif caca_palavras[y][x] == nome[index_letra]:
    if index_letra == len(nome) - 1:
      return nome
    else:
      return cacar(x, y-1, nome, index_letra + 1) + cacar(x+1, y-1, nome, index_letra + 1) +\
      cacar(x + 1, y, nome, index_letra + 1) + cacar(x + 1, y + 1, nome, index_letra + 1) +\
      cacar(x, y + 1, nome, index_letra + 1) + cacar(x - 1, y + 1, nome, index_letra + 1) +\
      cacar(x - 1, y, nome, index_letra + 1) + cacar(x - 1, y - 1, nome, index_letra + 1)
  else:
    return ""

#nomeia vilao:
def primeira_letra():
  vilao = ""
  for y in caca_palavras:
    for nome in viloes:
      if nome[0] in y:
        vilao = cacar(y.index(nome[0]), caca_palavras.index(y),nome, 0)
        if vilao != "":
          return nome
  
  return vilao

vilao = primeira_letra()
#printa de acordo com o resultado
if vilao == "CHARADA":
  print("Isso!!! Encontramos uma pista, mas somente o Charada está envolvido.")
elif vilao != "":
  if vilao == "REIDOSCONDIMENTOS":
    vilao = "Rei dos Condimentos"
  elif vilao == "DUASCARAS":
    vilao = "Duas Caras"
  else:
    vilao = vilao[0] + vilao[1:].lower()
  print(f"Isso!!! Encontramos uma pista, {vilao} está junto com o Charada.")
else:
  print("Poxa... acho que seguimos uma pista falsa.")