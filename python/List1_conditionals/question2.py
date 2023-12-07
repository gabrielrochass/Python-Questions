#zebrinha soltinha

#apostar nas zebras da copa
#contabilizar o dinheiro que ganhou ou perdeu
#infomrar o resultado do jogo e o lucro
#impedir apostas != zebra


#input

nome1 = input() # seleção da aposta sempre
nome2 = input()

aposta = int(input())
probabilidade_vitoria = float(input())

resultado = input()
valor = 0
#output

if probabilidade_vitoria >= 0.5:
  print(f'Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?')
else:   #calculo do lucro
  valor = int(aposta * (1 + ((0.5 - probabilidade_vitoria)**2) * 100))
  if resultado == 'Ganhou':
    if probabilidade_vitoria > 0.4 and probabilidade_vitoria < 0.5:
      print(f'Não foi um palpite tão arriscado, todos sabiam que {nome1} não estava muito atrás de {nome2}')
      print(f'Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta')
    elif probabilidade_vitoria <= 0.4 and probabilidade_vitoria > 0.3:
      print(f'Eu pensava que {nome2} iria ganhar, mas nunca duvidei que a {nome1} pudesse ganhar essa partida')
      print(f'Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta')
    elif probabilidade_vitoria > 0.2 and probabilidade_vitoria < 0.3:
      print(f'Uau! que jogo foi esse?? {nome1} surpreendeu a todos nós…')
      print(f'Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta')
    elif probabilidade_vitoria > 0.1 and probabilidade_vitoria < 0.2:
      print(f'Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {nome1} ganhou de {nome2}, alguém me explica?')
      print(f'Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta')
    elif probabilidade_vitoria <= 0.1:
      print(f'PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {nome1}, somente você!')
      print(f'Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta')
  else:
    print(f'Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…')
    print(f'Você poderia ter ganhado R${valor}, mas perdeu R${aposta}')

