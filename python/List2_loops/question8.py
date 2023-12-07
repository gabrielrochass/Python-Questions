#pipou
# atividades escolhidas pelo hotel
#imprimir o roteiro 

#input
#numero de entradas indeterminadas com as atividades diurnas -> while
fim = bool()
acabou = bool()
quantidade_atividades = 0
numero_atividades = 0
quantidade_noite = 0

Amor = False
Lancha = False
Pipa = False
chapadao = False
buggy = False
Tirolesa = False

gastronomico = False
centrinho = False
Luau = False
DJ = False

#output
print('Roteiro emitido!')
print('DIA:')
while not fim:
  atividade = input()
  if atividade == 'NOITE':
      fim = True
      break
  
  repeated = False
  if atividade == "Ir para a Praia do Amor":
    repeated = Amor or repeated
    Amor = True
  if atividade == "Passeio de Lancha":
    repeated = Lancha or repeated  
    Lancha = True
  if atividade == "Surf na Praia de Pipa":
    repeated = Pipa or repeated  
    Pipa = True
  if atividade == "Por do sol no chapadão":
    repeated = chapadao or repeated
    chapadao = True
  if atividade == "Passeio de buggy":
    repeated = buggy or repeated
    buggy = True
  if atividade == "Arborismo e Tirolesa":
    repeated = Tirolesa or repeated
    Tirolesa = True  
  
  if repeated or (atividade != 'Ir para a Praia do Amor' and  atividade != 'Passeio de Lancha' and atividade != 'Surf na Praia de Pipa' and atividade != 'Por do sol no chapadão' and atividade != 'Passeio de buggy' and atividade != 'Arborismo e Tirolesa'):
    print('[INVALIDO]')
  else:
    print(atividade)
    quantidade_atividades += 1
print('NOITE:') # 2 opções
i = 0
while not acabou:
  i += 1
  if quantidade_atividades % 2 == 1 and i > 2:
    break
  else:
    atividade_noite = input()
    if atividade_noite == 'Oba, Tudo planejado!!':
        acabou = True
        break
    
    repeated = False
    if atividade_noite == "Jantar gastronômico":
      repeated = gastronomico or repeated
      gastronomico = True
    if atividade_noite == "Passear pelo centrinho":
      repeated = centrinho or repeated
      centrinho = True
    if atividade_noite == "Luau":
      repeated = Luau or repeated
      Luau = True
    if atividade_noite == "Festa com DJ":
      repeated = DJ or repeated
      DJ = True
      
    if repeated or (atividade_noite != 'Jantar gastronômico' and atividade_noite != 'Passear pelo centrinho' and atividade_noite != 'Luau' and atividade_noite != 'Festa com DJ'):
      print('[INVALIDO]')
    else:
      print(atividade_noite)
      quantidade_noite += 1


numero_atividades = quantidade_atividades + quantidade_noite
print(f'Venha curtir esse dia em Pipa com um roteiro com {numero_atividades} atividade(s)!')



