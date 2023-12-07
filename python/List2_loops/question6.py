nome_invencao = input()
nome_etapa = ""
custo_total = 0
etapas_realizadas = 0
tentativas_falhas = 0
while True:
  nome_etapa = input()
  
  if nome_etapa == "concluir" or nome_etapa == "desistir":
    print(f"A jornada da construção do(a) {nome_invencao} acaba aqui.")
    break
  elif nome_etapa == "dar um plus":
    custo_etapa = int(input())
    custo_total += custo_etapa
    print(f"Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}")
  else:
    custo_etapa = int(input())
    num_tentativas = int(input())
    
    for i in range(num_tentativas):
      status = input()
      custo_total += custo_etapa
      if status == "correto":
        etapas_realizadas += 1
        print(f'Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}')
        break
      else: # incorreto
        tentativas_falhas += 1
        print(f'Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}')
    print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {tentativas_falhas}')

if nome_etapa == "desistir":
  print(f"Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${custo_total}")
else:
  print(f"Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${custo_total}")