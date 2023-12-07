#o alovo

# 4 amigos
#Uma pessoa X deverá dizer quantos dardos consegue acertar no alvo em 3 tentativas
#  pessoa X deve apostar um valor em si mesma

#Enquanto isso, as outras três pessoas poderão ou não apostar contra
#pelo menos uma pessoa sempre vai apostar contra


#regra 1: se x acertar, ganha tudo (apostados_contra + apostado_si)
#regra 2: se x errar, transfere o apostado_si para cada um dos 3 amigos


#M -> 3/3 e apostado_si = 100 // 2/3
#F, G e A apostado_contra = 120

#m: - 300 de saldo
#f g a: 100 de saldo

#computar os saldos e printar o resultado

#input:
quantidade_rodadas = int(input())
rodada = 1
saldo_a = 0
saldo_f = 0
saldo_g = 0
saldo_m = 0
exp_pos_jogada = ''
for i in range(quantidade_rodadas):
  tentativas = 3
  recebas = 0
  print(f'Rodada numero {rodada}')
  rodada +=1
  
  nome_jogador = input()
  print(f'Jogador: {nome_jogador}')
  
  aposta_si = int(input())
  print(f'Valor apostado: {aposta_si}')
  
  acertos_estimados = int(input())
  print(f'Acreditando que acerta {acertos_estimados} vezes em 3 tentativas')
  
  quantidade_amigos_contra = int(input())
  print(f'{quantidade_amigos_contra} amigos apostaram contra')
  
  if quantidade_amigos_contra == 3:
    print(f'Parece que {nome_jogador} está sendo subestimado!')
  
  valor_contra_total = 0
  a_aposta, f_aposta, g_aposta, m_aposta= 0, 0, 0, 0
  for i in range(quantidade_amigos_contra):
    nome_contra = input()
    valor_contra = int(input())
    if nome_contra == "Artur":
      a_aposta = valor_contra
    elif nome_contra == "Guga":
      g_aposta = valor_contra
    elif nome_contra == "Frej":
      f_aposta = valor_contra
    else:
      m_aposta = valor_contra
    valor_contra_total += valor_contra
    print(f'{nome_contra} apostou {valor_contra}')
  
  for _ in range(3):
    tentativas-=1
    exp_pos_jogada = input()
    if exp_pos_jogada == "Receba!":
      recebas += 1
    else:
      print(f'Errou! Restam {tentativas} tentativas')
  
  if recebas == acertos_estimados:
    if nome_jogador == "Artur":
      saldo_a += valor_contra_total
    elif nome_jogador == "Guga":
      saldo_g += valor_contra_total
    elif nome_jogador == "Frej":
      saldo_f += valor_contra_total
    else:
      saldo_m += valor_contra_total
    
   
    saldo_a -= a_aposta
    saldo_g -= g_aposta
    saldo_f -= f_aposta
    saldo_m -= m_aposta
  else:
    if nome_jogador == "Artur":
      saldo_a -= aposta_si * quantidade_amigos_contra
    elif nome_jogador == "Guga":
      saldo_g -= aposta_si * quantidade_amigos_contra
    elif nome_jogador == "Frej":
      saldo_f -= aposta_si * quantidade_amigos_contra
    else:
      saldo_m -= aposta_si * quantidade_amigos_contra
    
    if a_aposta > 0:
      saldo_a += aposta_si
    if g_aposta > 0:
      saldo_g += aposta_si
    if f_aposta > 0:
      saldo_f += aposta_si
    if m_aposta > 0:
      saldo_m += aposta_si
    
  #if input() == 'Receba!':
  #  recebas+= 1 
    
  #comparar quem ganha
  
print('Fim de jogo, o resultado foi:')
print(f'Artur ficou com {saldo_a} de saldo')
print(f'Frej ficou com {saldo_f} de saldo')
print(f'Guga ficou com {saldo_g} de saldo')
print(f'Misheldon ficou com {saldo_m} de saldo')


    

    