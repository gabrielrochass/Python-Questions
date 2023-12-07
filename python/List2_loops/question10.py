#ferias em las vegas

#regras
#ordem 1: colocar palavra de tras p frente
#ordem 2: colocar uma palavra em binario

#tabela ASCII e comando ord()

#cada participante -> 3 vidas
# if erro -> vida -= 1
#corrija as respostas e conte as vidas

#inputs:
vidas_calegario = 3
vidas_oponente = 3

while vidas_calegario > 0 and vidas_oponente > 0:
  palavra = input()
  acao = input()
  resposta = input()
  
  output = ""
  if acao == "1": # inverter
    invertida = ""
    for i in range(len(palavra)-1, -1, -1):
      invertida += palavra[i]
    if invertida == resposta:
      output = "apostador perdeu uma vida"
      vidas_oponente -= 1
    else:
      output = "calegario perdeu uma vida"
      vidas_calegario -= 1
  else: # binario
    binario = ""
    for c in palavra:
      c_int = ord(c)
      binario_invertido = ""
      quoc = c_int
      while quoc > 0:
        bit = quoc % 2
        binario_invertido += str(bit)
        quoc //= 2
      binario_c = ""
      for i in range(len(binario_invertido)-1, -1, -1):
        binario_c += binario_invertido[i]
      
      for _ in range(8 - len(binario_c)):
        binario_c = "0" + binario_c
      binario = binario + binario_c
    if binario == resposta:
      output = "apostador perdeu uma vida\nComo alguém consegue fazer isso de cabeça?"
      vidas_oponente -= 1
    else:
      vidas_calegario -= 1
      output = "calegario perdeu uma vida"
  print("Rodada Concluída!")
  print(output)

print("Partida Concluída!")
if vidas_calegario > 0:
  print("Vencedor: calegario")
  print("Droga, não acredito que eu perdi essa partida, achei que seria uma vitória fácil...")
else:
  print("Vencedor: apostador")
  print("HAHAHA, acha mesmo que preciso trapacear para ganhar de você?")
