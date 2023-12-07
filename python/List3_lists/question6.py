qt_decodificações = int(input())
list_prox_num = []

for i in range(qt_decodificações):
    codigo = input().split(' ')
    posicao_fibonacci = codigo[0]

    first = 0
    sec = 1
    if posicao_fibonacci == 0 or posicao_fibonacci == 1:
      print(posicao_fibonacci)
      
    else:  
      for prox_num in range(int(posicao_fibonacci)-1):
        prox_num = first + sec
        first = sec
        sec = prox_num
    
    prox_num = list(str(prox_num))
    lista_suporte = codigo[1].split('-')
    var = prox_num[int(lista_suporte[0])] + prox_num[int(lista_suporte[1])]
    
    print(chr(int(var)), end='')