tamanho_seq = int(input())
chave = int(input())
sequencia_final = []
sequencia = input().split(', ')
inteiros_seq = []
str_seq_final = []
putra_lista = []
numero = 0
soma_outra_lista = 0

# j = 0
# soma_seq =int(sequencia[j+1])


# print(sequencia)
#organizar as substituições na sequencia dada de acordo com a chave
if chave == 0: # ok
  for i in range(len(sequencia)):
    sequencia.remove(sequencia[0])
    sequencia_final.append('0')
  # print(sequencia_final)
  format_seq_final = ', '.join(sequencia_final)
  print(f'Não foi dessa vez Gideãozinho a chave corrompeu e a sequencia ficou assim: {format_seq_final}')
  
else:
  if chave < 0: #substituir pela soma dos dois termos anteriores
    for k in sequencia:
      int_k = int(k)
      inteiros_seq.append(int_k)
    inteiros_seq_x5 = inteiros_seq*20 #listaint
    for j in range(tamanho_seq):
        putra_lista = []
        for i in range(1,abs(chave) + 1):
          numero = inteiros_seq_x5[j - i]
          putra_lista.append(numero)
        soma_outra_lista = sum(putra_lista)
        sequencia_final.insert(j, soma_outra_lista)

    for m in sequencia_final:
      str_m = str(m)
      str_seq_final.append(str_m)
    # print(str_seq_final)
    format_seq_final = ', '.join(str_seq_final)
    # print(format_seq_final)
    print(f'Vamos lá Gideãozinho a sequencia final é {format_seq_final}')
      
  
  else: #chave > 0 ok
    for k in sequencia:
      int_k = int(k)
      inteiros_seq.append(int_k)
      inteiros_seq_x5 = inteiros_seq*20

    for j in range(tamanho_seq):
        putra_lista = []
        for i in range(1,abs(chave) + 1):
          numero = inteiros_seq_x5[i + j]
          putra_lista.append(numero)
        soma_outra_lista = sum(putra_lista)
        sequencia_final.append(soma_outra_lista)
    
    for m in sequencia_final:
      str_m = str(m)
      str_seq_final.append(str_m)
    # print(str_seq_final)
    format_seq_final = ', '.join(str_seq_final)
    # print(format_seq_final)
    print(f'Vamos lá Gideãozinho a sequencia final é {format_seq_final}')
