'''
nomescompostosjuntos

input

n = int(input()) -> numero de jogos em promoção
nome1 = input()
seq1 = input()
nome2 = input()
seq2 = input()
...
nomeN = input()
seqN = input()

output

se não for seq direta
print('Achamos {nome_jogo_promocao}, mas você ainda precisa jogar o 2, 3, …, (N-1) antes desse')

se for seq direta
print('Achei a sequel! Hora da diversão!')
'''

promo = int(input())

for i in range(promo):
    nome = input()
    seq = int(input())
    if seq == 2:
      print(f'Achei a sequel! Hora da diversão!')
    else:
      print(f'Achamos {nome} {seq}, mas você ainda precisa jogar o', end= ' ')
      for i in range(2, seq):
        if i < (seq -1):
          print(f'{i},', end=' ')
          i -=1  
        else:
          print(f'{i}', end=' ')
        #colocar a ordem das sequencias de forma crescente
      print(f'antes desse.')
    
        