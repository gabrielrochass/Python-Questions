# objetivo: escolha de um sucessor entre dois participantes

# sobre o bordão:
# 'PROOOO FUNDO DO GOOOL': + 15 pontos
# 'EU QUERO É GRITAR GOL': - 10 pontos

#o sucessor
# # objetivo: escolha de um sucessor entre dois participantes

# sobre o bordão:
# 'PROOOO FUNDO DO GOOOL': + 15 pontos
# 'EU QUERO É GRITAR GOL': - 10 pontos
# 'VOCÊ. É. RIDÍCULO': + 18 pontos
# 'QUEM SABE NA BOLA PARADA': - 5 pontos
# else: + 10 pontos

# carisma: + 10 pontos
# emoção: pontuação total + emoção do narrador

# input - características de dois narradores
# positivas: +
# negativa: -

#variável pontos

# nome_narrador_1
# nome_narrador_2

# bordao_narrador_1 -> str; sim/ não (booleano)
# bordao_narrador_2 -> str; sim/ não (booleano)

# é_carismatico_narrador_1
# é_carismatico_narrador_2

# emocao_narrador_1 -> int; 0 <= x <= 100
# emocao_narrador_2 -> int; 0 <= x <= 100

# output: mensagem
# O(a) narrador(a) escolhido(a) é {nome_narrador}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.
# não há empate

#narrador1
nome_narrador_1 = input()
bordao_narrador_1 = str(input())
eh_carismatico_1 = input()
emocao_narrador_1 = int(input())
ponto1 = 0

#narrador2
nome_narrador_2 = input()
bordao_narrador_2 = str(input())
eh_carismatico_2 = input()
emocao_narrador_2 =int(input())
ponto2 = 0

#pontuação narrador 1 bordão
if bordao_narrador_1 == 'PROOOO FUNDO DO GOOOL':
  ponto1 += 15

elif bordao_narrador_1 == 'EU QUERO É GRITAR GOL':
  ponto1 -= 10

elif bordao_narrador_1 == 'VOCÊ. É. RIDÍCULO':
  ponto1 += 18

elif bordao_narrador_1 == 'QUEM SABE NA BOLA PARADA':
  ponto1 -= 5
  
else:
  ponto1 += 10

#pontuação narrador 1 outros

if eh_carismatico_1 == 'sim':
 ponto1 += 10


total1 = int(ponto1 + emocao_narrador_1)

#pontuação narrador 2:

if bordao_narrador_2 == 'PROOOO FUNDO DO GOOOL':
  ponto2 =+ 15

elif bordao_narrador_2 == 'EU QUERO É GRITAR GOL':
  ponto2 =- 10

elif bordao_narrador_2 == 'VOCÊ. É. RIDÍCULO':
  ponto2 =+ 18

elif bordao_narrador_2 == 'QUEM SABE NA BOLA PARADA':
  ponto2 =- 5

else:
  ponto2 += 10

# pontuação narrador 2 outros

if eh_carismatico_2 == 'sim':
  ponto2 += 10
else:
  ponto2 += 0

total2 = int(ponto2 + emocao_narrador_2)

#comparativo
if total1 > total2:
  print(f'O(a) narrador(a) escolhido(a) é {nome_narrador_1}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')
    
else:
  print(f'O(a) narrador(a) escolhido(a) é {nome_narrador_2}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')
 