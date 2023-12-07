#bilhete premiado 

#sortear um número binário
#converter para decimal
#acertou a conversão = ganhou

#receber o número sorteado
#converter para binário
#verificar se acertou

# 3 chances: diz o prox palpite se tiver errado o anterior
#verificar qual o destino premiado
#1: porto de galinhas
#2: fernando de noronha
#3: gramado
#4:berlim
#5: tóquio


#INPUTS:
n_binario = input()[::-1] #primeiro numero sorteado em binário
chances = 3
palpite = 0
resultado = 0
# while chances != 0 or palpite != resultado:
for i in range(3,0,-1):
  expoente = 0
  for i in n_binario:
    numero = "1"
    if i == numero:
      resultado += 2**expoente
    expoente += 1
  palpite = int(input()) #valor na base decimal
  chances -= 1
  # numero_digitado = palpite
  # quociente = 1
  # lista = []
  # while quociente >= 1:
  #   resto = palpite % 2
  #   lista.insert(0,resto)
  #   quociente = palpite // 2
  #   palpite = quociente
  # binario = ''.join([str(i) for i in lista])
  if palpite == resultado:
    print(f'Parabéns!! Você acertou!')
    
    if palpite == 1:
      print('Férias inesquecíveis estão te esperando!') 
      print('Seu destino será Porto de Galinhas (BRA).')
      print('Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!')
    elif palpite == 2:
      print('Férias inesquecíveis estão te esperando!')
      print('Seu destino será Fernando de Noronha (BRA).')
      print('Belíssimas praias estão por vir.')
      print('Não esqueça o protetor solar.')
     
    elif palpite == 3:
      print('Férias inesquecíveis estão te esperando!')
      print('Seu destino será Gramado (BRA).')
      print('Aproveite passeios e paisagens espetaculares no sul do país!')
    
    elif palpite == 4:
      print('Férias inesquecíveis estão te esperando!')
      print('Seu destino será Berlim (ALE).')
      print('Desfrute de muita cultura e de experiências incríveis!')
      print('Prepare os casacos de frio!')
     
    elif palpite == 5:
      print('Férias inesquecíveis estão te esperando!')
      print('Seu destino será Tóquio (JPN).')
      print('Viva uma experiência inesquecível explorando um país do outro lado do mundo.')
      print('Prepare-se para muitas horas de voo!')
      
    else:
      print('Mas, infelizmente, hoje não é o seu dia de sorte.')
      print('Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.')
      print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
    
    break
  
  else:
    chances-= 1
    if chances != 0:
      print(f'Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).')
    else:
      chances == 0