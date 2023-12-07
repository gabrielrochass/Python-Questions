dias = int(input())
casas = int(input())
ticks = (24000 * 9 * dias)/ 2

ticks_casa = ticks / casas
print(f'{ticks_casa:.0f}')