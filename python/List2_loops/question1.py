'''
saber quantos aliens são derrotados por dia
código que recebe frases

a contagem para quando:
1. o dia acabou
2. o relógio descarregou

input

número indeterminado de inputs - while
 variável +=1 (contabilizados como aliens derrotados)
 
if input('o relógio descarregou' or 'por hoje já deu') -> finaliza contagem

output

Caso a frase seja: ‘O relógio descarregou!':
ptint(“Corra Ben! Você já derrotou {contador} aliens”)

Caso a frase seja: ‘Por hoje já deu':
print(“Muito Ben Ben! hehe você derrotou {contador} aliens hoje”)
'''

aliens = 0

frase = input()

while (frase != 'O relógio descarregou!') and (frase != 'Por hoje já deu'):
  aliens += 1
  frase = input()
else: 
  if frase == 'O relógio descarregou!':
    print(f'Corra Ben! Você já derrotou {aliens} aliens')
  else:
    print(f'Muito Ben Ben! hehe você derrotou {aliens} aliens hoje')
  
  
  
  
  
  
  