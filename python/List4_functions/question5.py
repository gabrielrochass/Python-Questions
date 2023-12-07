def prints(vitoria, derrotas, empates):
  if vitorias == 3:
    print("Nenhum dos 3 inimigos foram capazes de derrotar o Denji!")
  elif derrotas == 3:
    print("Hoje não foi um dia bom para o Denji, perdeu todas as batalhas")
  elif vitorias == 1 and derrotas == 1:
    print("Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar")
  elif vitorias > derrotas and vitorias > empates:
    print("Denji conseguiu derrotar a maioria de seus inimigos")
  elif derrotas > vitorias and derrotas > empates:
    print("Dia péssimo para o Denji, perdeu a maioria de suas batalhas")
  elif empates > derrotas and empates > vitorias:
    print("Dia duro para o Denji, empatou de mais")

def trasf_denj(energia, controle, precisao):
  if energia>=750 and controle>=7 and precisao>= 8:
    return "Motosserra Suprema"
  elif energia>=500 and controle >= 6 and precisao>= 6:
    return "Motosserra Avançada"
  else:
    return "Motosserra Normal"

def enemy_rodada(rodada):
  if rodada == 1:
    return "Makima"
  elif rodada == 2:
    return "Reze"
  return "Santa Claus"

def winner_fim(forca_denji, forcaVilao):
  if forca_denji > forcaVilao:
    return "denji"
  elif forcaVilao > forca_denji:
    return "vilao"
  return "empate"

batalhas = []
vitorias = 0
derrotas = 0
empates = 0

for rodada in range(1, 4):

  energia = int(input())
  controle = int(input())
  precisao = int(input())
  transformacao = trasf_denj(energia, controle, precisao)
  forca_denji = energia + (controle * precisao)
  forca_enemy = int(input())
  nome_vilao = enemy_rodada(rodada)

  print(f"### Rodada {rodada} - {nome_vilao} ###")
  print(f"O Denji ira se transformar na {transformacao} para enfrentar o {nome_vilao}")

  winner_rodada = winner_fim(forca_denji, forca_enemy)
  if winner_rodada == "denji":
    print(f"Denji saiu vitorioso nessa batalha contra o {nome_vilao}")
    batalhas.append([rodada, transformacao, "Vitoria"])
    vitorias += 1
  elif winner_rodada == "vilao":
    print(f"Denji não conseguiu força o suficiente para derrotar o {nome_vilao}")
    batalhas.append([rodada, transformacao, "Derrota"])
    derrotas += 1
  elif winner_rodada == "empate":
    print(f"Como pode ser possível?? Denji possui a mesma força que o {nome_vilao}")
    batalhas.append([rodada, transformacao, "Empate"])
    empates += 1

print("### Resultado Final ###")
for i in batalhas:
  print(f"Rodada {i[0]}: {i[1]} - {i[2]}")

prints(vitorias, derrotas, empates)
