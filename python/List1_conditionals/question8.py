#em busca do craque
#análise do número de bolas colocadas na área por cada jogador nas suas últimas partidas

# if empate:
# #calculo taxa de finalizações convertidas em gol:  (gols/finalizações) * 100.

#12 entradas: 4 para jogador1 e 4 para jogador2

#inputs
nome1 = input()
bolas_area1 = int(input())
chutes1 = int(input())
gols1 = int(input())
taxa1 = (gols1/chutes1) * 100
resultado1 = bolas_area1

nome2 = input()
bolas_area2 = int(input())
chutes2 = int(input())
gols2 = int(input())
taxa2 = (gols2/chutes2) * 100
resultado2 = bolas_area2

nome3 = input()
bolas_area3 = int(input())
chutes3 = int(input())
gols3 = int(input())
taxa3 = (gols3/chutes3) * 100
resultado3 = bolas_area3

#output
#empates em primeiro:
if bolas_area1 == bolas_area2 and bolas_area2 > bolas_area3:
    resultado1 = taxa1
    resultado2 = taxa2
    resultado3 = 0
    print(f'Tite está mais indeciso do que nunca!')

if bolas_area1 == bolas_area3 and bolas_area3 > bolas_area2:
    resultado3 = taxa3
    resultado1 = taxa1
    resultado2 = 0
    print(f'Tite está mais indeciso do que nunca!')

if bolas_area2 == bolas_area3 and bolas_area3 > bolas_area1:
    resultado2 = taxa2
    resultado3 = taxa3
    resultado1 = 0
    print(f'Tite está mais indeciso do que nunca!')

#empates em segundo

if bolas_area1 > bolas_area2 and bolas_area2 == bolas_area3:
    resultado1 = 101
    resultado2 = taxa2
    resultado3 = taxa3

if bolas_area2 > bolas_area1 and bolas_area1 == bolas_area3:
    resultado2 = 101
    resultado1 = taxa1
    resultado3 = taxa3

if bolas_area3 > bolas_area1 and bolas_area1 == bolas_area2:
    resultado3 = 101
    resultado1 = taxa1
    resultado2 = taxa2

if bolas_area3 == bolas_area1 and bolas_area1 == bolas_area2:
    resultado3 = taxa3
    resultado1 = taxa1
    resultado2 = taxa2
    print(f'Tite está mais indeciso do que nunca!')

 #taxas para desempatar
if resultado1 > resultado2 and resultado2 > resultado3:
    print(f'{nome1}\n{nome2}\n{nome3}')
    if bolas_area1 <= 10:
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome1}?! Sei não hein Galvão…')
    else: 
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome1}! Dessa vez o hexa vem pra casa!!')

if resultado1 > resultado3 and resultado3 > resultado2:
    print(f'{nome1}\n{nome3}\n{nome2}')
    if bolas_area1 <= 10:
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome1}?! Sei não hein Galvão…')
    else: 
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome1}! Dessa vez o hexa vem pra casa!!')

if resultado2 > resultado1 and resultado1 > resultado3:
    print(f'{nome2}\n{nome1}\n{nome3}')
    if bolas_area2 <= 10:
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome2}?! Sei não hein Galvão…')
    else: 
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome2}! Dessa vez o hexa vem pra casa!!')

if resultado2 > resultado3 and resultado3 > resultado1:
    print(f'{nome2}\n{nome3}\n{nome1}')
    if bolas_area2 <= 10:
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome2}?! Sei não hein Galvão…')
    else: 
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome2}! Dessa vez o hexa vem pra casa!!')

if resultado3 > resultado1 and resultado1 > resultado2:
    print(f'{nome3}\n{nome1}\n{nome2}')
    if bolas_area3 <= 10:
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome3}?! Sei não hein Galvão…')
    else: 
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome3}! Dessa vez o hexa vem pra casa!!')

if resultado3 > resultado2 and resultado2 > resultado1:
    print(f'{nome3}\n{nome2}\n{nome1}')
    if bolas_area3 <= 10:
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome3}?! Sei não hein Galvão…')
    else: 
        print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…\n{nome3}! Dessa vez o hexa vem pra casa!!')





