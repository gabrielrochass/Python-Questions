#mostra tua força brasil
#pode avançar quanto ser eliminado a qualquer momento

#PERDER:
#if brasil perder antes da final = eliminado e não recebe entradas

#EMPATAR:
#else: recebe outros inputs
#favoritismo = fator de desempate
#if favoritismo1 = 2 - brasil passa

#GANHAR:
#favoritismo aumenta com o placar do jogo
#if gols_brasil - gols_outro > 1
#favoritismo1 += 10

#if gols_brasil - gols_outro > 2
#favoritismo1 += 20

#if gols_brasil - gols_outro > 3
#favoritismo1 += 30

#FINAL

#SÓ SABE O OPONENTE E O FAVORTISMO QUE CHEGA
#o favoritismo define o campeão - empate, brasil ganha

#3 partidas + final, caso passe

##inputs

#oitavas
fav_br = int(input())
oponente1 = input()
fav_oponente1 = int(input())
gols_br1 = int(input())
gols_oponente1 = int(input())
# isClassified = bool()

#brasil eliminado no jogo1

if gols_br1 == gols_oponente1 and fav_br < fav_oponente1:
  print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
elif gols_br1 < gols_oponente1:
  print(f'Infelizmente essa seleção dx {oponente1} era muito forte para o Brasil.')

#passa pra próxima fase:
elif gols_br1 == gols_oponente1 and fav_br >= fav_oponente1: ##ganhe o jogo 1 por fav (a)
  print('No sufoco, o Brasil conseguiu ganhar!!!')
elif gols_br1 > gols_oponente1:
  print('Quem é que segura o Brasil???')
  

if (gols_br1 > gols_oponente1) or (gols_br1 == gols_oponente1 and fav_br >= fav_oponente1):
  oponente2 = input()
  fav_oponente2 = int(input())
  gols_br2 = int(input())
  gols_oponente2 = int(input())
  #aumento do fav1
  if gols_br1 - gols_oponente1 == 1:
    fav_br += 10
  elif gols_br1 - gols_oponente1 == 2:
    fav_br += 20
  elif gols_br1 - gols_oponente1 >= 3:
    fav_br += 30

#eliminado no jogo2
  if gols_br2 < gols_oponente2:
    print(f'Infelizmente essa seleção dx {oponente2} era muito forte para o Brasil.')    
  elif gols_br2 == gols_oponente2 and fav_br < fav_oponente2:
    print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
  
  #passa pra próxma fase
  elif gols_br2 == gols_oponente2 and fav_br >= fav_oponente2:
    print('No sufoco, o Brasil conseguiu ganhar!!!')
  elif gols_br2 > gols_oponente2:
    print(f'Quem é que segura o Brasil???')
    
  if (gols_br2 > gols_oponente2) or (gols_br2 == gols_oponente2 and fav_br >= fav_oponente2):
    oponente3 = input()
    fav_oponente3 = int(input())
    gols_br3 = int(input())
    gols_oponente3 = int(input())
  #aumento do fav2
    if gols_br2 - gols_oponente2 == 1:
      fav_br += 10
    elif gols_br2 - gols_oponente2 == 2:
      fav_br += 20
    elif gols_br2 - gols_oponente2 >= 3:
      fav_br += 30

#eliminado no jogo3
    if gols_br3 < gols_oponente3:
      print(f'Infelizmente essa seleção dx {oponente3} era muito forte para o Brasil.')
    elif gols_br3 == gols_oponente3 and fav_br < fav_oponente3:
      print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
#passa pra próxima fase:
    elif gols_br3 == gols_oponente3 and fav_br >= fav_oponente3:
      print('No sufoco, o Brasil conseguiu ganhar!!!')
    elif gols_br3 > gols_oponente3:
      print(f'Quem é que segura o Brasil???')
     
    if (gols_br3 > gols_oponente3) or (gols_br3 == gols_oponente3 and fav_br >= fav_oponente3):
      oponente4 = input()
      fav_oponente4 = int(input())
      #aumento do fav3
      if gols_br3 - gols_oponente3 == 1:
        fav_br += 10
      elif gols_br3 - gols_oponente3 == 2:
        fav_br += 20
      elif gols_br3 - gols_oponente3 >= 3:
        fav_br += 30
#vencedor da ultima rodada
      if fav_br < fav_oponente4:
        print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
      elif fav_br >= fav_oponente4:
        print('O BRASIL VAI SER HEXAAAAAAAA')
