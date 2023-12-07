#calcula a razão:
def razao(elementos_inteiros):
  return elementos_inteiros[1] - elementos_inteiros[0]
  
#calcula o resultado da pa:
def pa(elementos_inteiros, posicao, razao_final):
  if posicao == 1:
    return elementos_inteiros[1]
  elif posicao == 2:
    return elementos_inteiros[2]
  elif posicao == 3:
    return elementos_inteiros [3]
    
  else:
    return elementos_inteiros[-1] + (razao_final*(posicao-3))
  

#recebe 3 numeros inteiros
elementos = input().split(' ')

#transforma para inteiros e os colocar em uma lista de inteiros
elementos_inteiros = []
for i in range(len(elementos)):
  elementos_inteiros.append(int(elementos[i]))
# print(elementos_inteiros)

#recebe a posicao do elemento a ser buscado na progressao aritimética
posicao = int(input())

#recebe as funções
razao_final = razao(elementos_inteiros)
# print(x)

#recebe o resultado da pa
resultado_pa = pa(elementos_inteiros, posicao, razao_final)
# print(y)

#saída final:
format_elementos = ', '.join(elementos[0:2])
print(f'Na progressão aritmética cujos três primeiros números são {format_elementos} e {elementos[2]}, o {posicao}º elemento é {resultado_pa} e a razão da progressão é {razao_final}.')




