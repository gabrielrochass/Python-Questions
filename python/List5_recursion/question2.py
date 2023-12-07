#ordena minha string
def inverterString(string, contador):
    if contador == 0:
      return string[contador]
    else:
      return string[contador] + inverterString(string, contador-1)

#recebe uma string com apenas letras na ordem reversa 
entrada = input()

# imprime de forma correta
print(inverterString(entrada, len(entrada)-1))