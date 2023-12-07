def primo():
  multiplos = 0
  
  if num == 1:
      print(f'O número {num} não é primo.')
      print(f'Além disso, não temos primos no intervalo de 1 à {num}.')
  else:
    
    for i in range(2, num):
      if num % i == 0:
        multiplos += 1
          
    if multiplos > 0:
      print(f'O número {num} não é primo.')
      primos = []
          
      for j in range(num, 2, -1):
        multiplos = 0

        for k in range(j - 1, 1, -1):
          if j % k == 0:
            multiplos += 1

        if multiplos == 0:
          primos.append(j)

      if len(primos) > 0:
        print(f'Entretanto, temos primos no intervalo de 1 à {num}. Estes são:')
        print('2',end=', ')
        primos = list(reversed(primos))
        for numero in range(len(primos)-1):
          print(primos[numero],end=', ')
        print(primos[-1])  
      else:
        print(f'Além disso, não temos primos no intervalo de 1 à {num}.')
    else:
      print(f'O número {num} é primo.')

  print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')

num = int(input())
primo()
