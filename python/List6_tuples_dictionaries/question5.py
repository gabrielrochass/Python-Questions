# determinar o quão cansada tá a dog

# inicia com energia max -> max q ela pode atingir
# while energia > 0 and gasto < 100: procura brinquedo

# if gasto > energia: energia = 0
# gasto n reduz, só aumenta

# vaquinha:
# energia perdida = numero de chaquoalhadas

# chupeta:
# energia_atual = max(n de mordidas, energia_atual - 5)

# ze gotinha:
# energia_atual = energia_atual // n de apertos
# if / == 0: energia_atual permanece a mesma

# bolinha:
# energia_atual = energia_atual - (velocidade // 4)

# osso:
# energia_atual = energia_atual + 2. roidas

# comida:
# if len(comida) % 2 == 0: energia_atual = energia_atual + len(comida)
# else: energia_atual = energia_atual - len(comida)

def vaquinha(energia, gasto, valor): #ok
  valor = int(valor)
  energia_anterior = energia
  energia = max(energia - valor, 0)
  gasto += min(energia_anterior - energia, 100)
  print('Brinquedo da vaquinha! Vou chacoalhar')
  # print(energia)
  # print(gasto)
  return energia, gasto  


def chupeta(energia, gasto, valor): #ok
  valor = int(valor)
  gasto += min(5, max(energia - valor, 0))
  energia_anterior = energia
  energia = max(valor, energia - 5)
  energia = max(energia, 0)
  energia = min(energiaComp, energia)
  print('Minha pipeta! Vou morder')
  # print(energia)
  # print(gasto)
  gasto = min(gasto, 100)
  return energia, gasto
  
  
def zegotinha(energia, gasto, valor):
  energiaParcial = 0
  valor = int(valor)
  # valor = min(valor, energia)
  valor = max(valor, 1)
  energiaParcial = energia // valor
  gasto += (energia - energiaParcial)
  energia = min(energia, energiaParcial)
  print('Meu preferido! Faz barulho e mordo')
  energia = max(energia, 0)
  # gasto = min(energiaComp, gasto)
  # print(energia)
  # print(gasto)
  return energia, gasto
  
  

def bolinha(energia, gasto, valor): #ok
  energiaParcial = 0
  valor = int(valor)
  energiaParcial = energia - (valor // 4)
  gasto += (energia - energiaParcial)
  energia = min(energia, energiaParcial)
  energia = max(energia, 0)
  # print(energia)
  # print(gasto)
  print('ZOOOOOOOOOOOOOOOOOM')
  gasto = min(gasto, 100)
  return energia, gasto
  
  
def osso(energia, gasto, valor): #ok
  valor = int(valor)
  energia = min(energiaComp, energia + (valor*2))
  print('Pausa para roer')
  energia = max(energia, 0)
  # print(energia)
  # print(gasto)
  return energia, gasto

  
def comida(energia, gasto, valor): #ok
  gasto = min(100, min(gasto - min(len(valor)*(-1)**len(valor), 0), gasto + energia))
  energia += min((len(valor)*((-1)**len(valor))), energiaComp)
  # gasto = max(energiaParcial, energia)
  print(f'Uhh, {valor} deve ser comestível')
  # energia = min(energia, energiaParcial)
  energia = max(energia, 0)
  # print(energia)
  # print(gasto)
  return energia, gasto

#recebe energiaMax
energiaMax = int(input())
energiaComp = energiaMax
# print(energiaMax)
gastoTotal = 0

#organiza info
informacoes = {'Vaquinha': int, 'Chupeta': int, 'Zé Gotinha': int, 'Bolinha': int, 'Osso': int, 'Comida': str}
funcoes = {'Vaquinha': vaquinha, 'Chupeta': chupeta, 'Zé Gotinha': zegotinha, 'Bolinha': bolinha, 'Osso': osso, 'Comida': comida}

while energiaMax > 0 and gastoTotal <= 100: # PQ O VALOR QUE RETORNA NA FUNÇÃO NÃO É RECEBIDO POR energiaMax E gastoTotal
  entrada = input().split(': ')
  # print(entrada)
  informacoes[entrada[0]] = entrada[1]
  # print(informacoes)
  (energiaMax, gastoTotal) = funcoes[entrada[0]](energiaMax, gastoTotal, informacoes[entrada[0]])
  # energiaMax, gastoTotal = (energia, gasto)
  # Vaquinha(energiaMax, gastoTotal, informacoes[entrada[0]])

gastoTotal = min(gastoTotal,100)
n = max(gastoTotal//10,1)
print(f"Mamãe chegou! Gastei {gastoTotal} pontos da minha energia e estou c{'a'*n}nsada, mas vou correr para seus braços!")
