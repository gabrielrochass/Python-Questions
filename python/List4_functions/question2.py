#armazenar nomes e chance de matar ele 
#if chance < 50%: bom partido
# else: evitar

#if len(nomes[i]) > 7: remove(i)

#if nomes[i] == 'Makima': bom partido

#input

def probabilidade(nome):
  global lista_final
  global matar
  global namorar
  if (len(nome) > 7):
    print(f'Er {nome[0]}{nome[1]}.. errr... nao consigo lembrar, melhor deixar para la')
  else:
    if (nome == 'Makima'):
      print(f"Woof Woof")
      chance = int(input())
      print(f"Beleza {nome}!! Essa é uma boa pretendente!")
      namorar += 1
    else:
      chance = int(input())
      if (chance > 50):
        print(
          f"{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?")
        matar += 1
        if (lista_final == ''):
          lista_final += f'nome: {nome} - chances de morrer: {chance}%'
        else:
          lista_final += f'\nnome: {nome} - chances de morrer: {chance}%'
      elif (chance <= 50):
        print(f"Beleza {nome}!! Essa é uma boa pretendente!")
        namorar += 1
        if (lista_final == ''):
          lista_final += f'nome: {nome} - chances de morrer: {chance}%'
        else:
          lista_final += f'\nnome: {nome} - chances de morrer: {chance}%'


matar = 0
namorar = 0
lista_final = ''
entrada = input()
while (entrada != 'cabo'):
  probabilidade(entrada)
  entrada = input()

if (namorar > matar):
  print("Epa ai sim! E hoje pochita!!")
else:
  print("Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos")

if (matar == 0):
  print(lista_final)


