def lutas(demonios, vida_denji, vida_demon, vida_demon_incial, ataque_denji, ataque_demon, ataque_demon_inicial, qt_mortos, duplicou):

  print(f'DENJI')
  print(f'Vida: {vida_denji}')
  print(f'Ataque atual: {ataque_denji}')

  print(f'DEMÔNIO')
  print(f'Vida: {vida_demon}')
  print(f'Ataque atual: {ataque_demon}')

  entrada_denji = input()
  if (entrada_denji == 'Denji ganhou um beijo de Makima'):
    vida_denji += 50
  elif (entrada_denji == 'Pochita chegou para a batalha!'):
    ataque_denji += 50
  elif (entrada_denji == 'Makima disse que ME AMA!!!'):
    vida_denji = int(vida_denji * 1.5)
  entrada_demon = input()
  if (entrada_demon == 'O demônio achou um escudo no chão!'):
    vida_demon += 25
  elif (entrada_demon == 'Onde ele arrumou essa espada?'):
    ataque_demon += 20
  elif (entrada_demon == 'Como assim ele se duplicou??!!'):
    duplicou = True
    vida_demon = 2 * vida_demon
    ataque_demon = 2 * ataque_demon

  vida_demon -= ataque_denji
  if (vida_demon <= 0):
    demonios -= 1
    if (duplicou == True):
      qt_mortos += 2
      duplicou = False
    else:
      qt_mortos += 1

    if (demonios > 0):
      print('Matei um!!!')
      vida_demon = vida_demon_incial
      ataque_demon = ataque_demon_inicial
      if (demonios > 0):
        vida_denji -= ataque_demon
  else:
    if (demonios > 0):
      vida_denji -= ataque_demon

  return demonios, vida_denji, vida_demon, vida_demon_incial, ataque_denji, ataque_demon, ataque_demon_inicial, qt_mortos, duplicou


duplicou = False
demonios = int(input())
qt_demon_inicial = demonios
qt_mortos = 0
end = False

if (demonios == 0):
  print('Uhuuul um dia só para relaxar!')
  end = True
else:
  vida_denji = int(input())
  vida_demon = int(input())
  vida_demon_incial = vida_demon
  ataque_denji = int(input())
  ataque_demon = int(input())
  ataque_demon_inicial = ataque_demon

  while (demonios > 0 and vida_denji > 0):
    demonios, vida_denji, vida_demon, vida_demon_incial, ataque_denji, ataque_demon, ataque_demon_inicial, qt_mortos, duplicou = lutas(demonios, vida_denji, vida_demon, vida_demon_incial, ataque_denji, ataque_demon, ataque_demon_inicial, qt_mortos, duplicou)


if (end == False):
  if (vida_denji <= 0):
    print('Infelizmente Denji foi de comes e bebes :(')
  elif (qt_mortos > qt_demon_inicial):
    print('Foi mais do que eu esperava mas finalmente terminei…')
  else:
    print('Ufa, agora posso descansar em paz!')