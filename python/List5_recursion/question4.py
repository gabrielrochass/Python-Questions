fibonacci = [0,1]
start = input().split()
end = input()
lista = input().split()

for i in range(len(lista)):
  lista[i] = int(lista[i])
matriz = []

for i in range(7):
  matriz.append(input().split())

def fib(index):
  if len(fibonacci) < index + 1:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fib(index)
  else:
    return fibonacci[index]

def busca_binaria(num, minimo, maximo):
  meio = int((minimo + maximo)/2)
  if lista[meio] == num:
    return meio

  elif num > lista[meio]:
    return busca_binaria(num, meio + 1, maximo)

  else:
    return busca_binaria(num, minimo, meio - 1)
    
def achar_nota(a,b,n):
  if matriz[b][a] == end:
    return n

  else:
    k = int(matriz[b][a][0:3],2)
    n += (k*fib(k))%7
    direcao = matriz[b][a][3:5]

    if direcao == "00":
      return achar_nota(a, b - 1, n)
      
    elif direcao == "01":
      return achar_nota(a + 1, b, n)
      
    elif direcao == "10":
      return achar_nota(a, b + 1, n)
      
    else:
      return achar_nota(a-1,b,n)

print(f"De acordo com a análise da matriz, a nota do aluno foi:\
 {busca_binaria(achar_nota(int(start[1]),int(start[0]),0),0,11)}")