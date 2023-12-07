a10 = 'Arthur'
l30 = 'Luiz'
p100 = 'Pedro'
precisa_mais = 'Nenhum'

D = int(input())

if (D <= 10):
  print(a10)

elif (10 < D <= 30):
 print(l30)

elif (30 < D <= 100):
 print(p100)

elif(D>100):
  print(precisa_mais)
