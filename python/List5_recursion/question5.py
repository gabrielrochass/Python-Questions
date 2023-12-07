#declara variáveis
intervalos = []

#recebe os inputs
lista = input().split(", ")

#acha intervalo
def achar_intervalo(intervalo):
  if len(lista):
    if not(len(intervalo)):
      intervalo = [int(lista.pop(0))]

    if len(lista) and int(lista[0]) - 1 == intervalo[-1]:
      intervalo.append(int(lista.pop(0)))

      if len(lista):
        return achar_intervalo(intervalo)

    intervalos.append(intervalo)
    return achar_intervalo([])

  else:
    if len(intervalos) > 0:
      intervalo = intervalos.pop(0)
      if len(intervalo) > 1:
        print(f"[{intervalo[0]}-{intervalo[-1]}]", end="")

      else:
        print(f"[{intervalo[0]}]", end="")
      
      if len(intervalos):
        print(", ", end="")
      return achar_intervalo([])

    else:
      return None
    
achar_intervalo([])