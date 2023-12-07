nome_inimigo = input()
nome_aliado = input()
clima_atual = input()
list_mensagens = []
# print("hi")
while 1:
  mensagem = input()
  if mensagem != "Cansado":
    mensagem = mensagem.split()
    list_mensagens.append([])
    for i in mensagem:
      list_mensagens[-1].append(int(i))
  else:
    break;
# print(list_mensagens)
done = True
if clima_atual == "Ensolarado":
  for mensagem in list_mensagens:
    for i in range(9):
      smallest = mensagem[i]
      index = i;
      for j in range(i + 1, len(mensagem)):
        if mensagem[j] < smallest:
          smallest = mensagem[j]
          index = j
      mensagem[index] = mensagem[i]
      mensagem[i] = smallest
      
  print(f"Caramba! Finalmente organizamos a mensagem secreta do {nome_inimigo} com esse clima Ensolarado! Vamos nessa {nome_aliado}!")
elif clima_atual == "Nublado":
  for mensagem in list_mensagens:
    for i in range(9):
      biggest = mensagem[i]
      index = i;
      for j in range(i + 1, len(mensagem)):
        if mensagem[j] > biggest:
          biggest = mensagem[j]
          index = j
      mensagem[index] = mensagem[i]
      mensagem[i] = biggest
  print(f"Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nome_inimigo}! Vamos nessa {nome_aliado}!")
elif clima_atual == "ChuvosoNormal":
  for lista in range(len(list_mensagens)-1):
    numero = 0
    for i in range(9):
      if list_mensagens[lista][i] < list_mensagens[lista+1][i]:
        num = list_mensagens[lista][i]
        list_mensagens[lista][i] = list_mensagens[lista+1][i]
        list_mensagens[lista+1][i] = num
    
  print(f"Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nome_inimigo}! Vamos nessa {nome_aliado}!")
elif clima_atual == "ChuvosoComRaio":
  for lista in range(len(list_mensagens)-1):
    numero = 0
    for i in range(9):
      if list_mensagens[lista][i] > list_mensagens[lista+1][i]:
        num = list_mensagens[lista][i]
        list_mensagens[lista][i] = list_mensagens[lista+1][i]
        list_mensagens[lista+1][i] = num
        
  print(f"Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nome_inimigo}! Vamos nessa {nome_aliado}!")
else:
  print("Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??")
  print(f"Tenho certeza que conseguiremos na próxima {nome_aliado}")
  done = False

if done:
  
  print(f"Agora decodificamos as {len(list_mensagens)} mensagens do {nome_inimigo} e sabemos seus {len(list_mensagens)} lugares de ataque.")
  print("Os lugares sao:")
  lugar = 0
  for m in list_mensagens:
    lugar += 1
    print(f"{lugar} lugar:")
    print(f"Coordenadas: {m[0]}° {m[1]}' {m[2]}''")
    print(f"Horario: {m[3]}h {m[4]}m {m[5]}s")
    print(f"Data: {m[6]}/{m[7]}/{m[8]}")
  print(f"Vamos rapido {nome_aliado}!!")
# print(msg)