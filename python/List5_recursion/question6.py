#converte hora
def converter (hora, periodo):
  if hora == 12 and periodo == "am":
    return 0
  elif periodo == "pm":
    if hora == 12:
      return 12
    return hora + 12
  return hora

#calcula chance de ataque
def calcular_chance(hora_atual, hora_final, qt_banhistas, chance):
  if hora_atual >= 6 and hora_atual <= 15:
    ratio = 2
    mod = 7
  else:
    ratio = 1
    mod = 10
  if hora_atual == 5:
    chance = 5
  elif hora_atual%2:
    chance += chance%mod
  else:
    chance += qt_banhistas/ratio
  if hora_atual == hora_final:
    return chance
  return calcular_chance((hora_atual+1)%24, hora_final, qt_banhistas, chance)

inicio = 5
hora = input().split()
hora[0] = int(hora[0])
hora_final = converter(hora[0], hora[1])
qt_banhistas = int(input())

#verifica validade
if qt_banhistas < 0 or hora[0] > 12 or hora[0] < 1:
  print("Dados Invalidos.")
else:
  chance = calcular_chance(inicio,hora_final, qt_banhistas, 0)
  print("A chance de aparecimento de Tubarao e de {0:.1f}%.".format(chance))
  if chance >= 100:
    print("E hoje que ele aparece.")