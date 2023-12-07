# decodificar uma mensagem
# composta por simbolos, numeros e letras

# palavra decodificadora
# ações definidas pelos inputs: portal, experimento, schembulovk e realidade

# input
#recebe o total de palavras que vai precisar decodificar:

total_palavras = int(input())
#palavra_codificada_sem_carac_especial = []
numeros = [0,1,2,3,4,5,6,7,8,9]
int_j = 0
end = ''
par = []
produto = 0
indice_j = 0
indice_proximaletra = 0
soma_par = 0
impar = []
soma_impar = 0
termos_tobemultiplicados = 0
palavra_final = ''
resposta = []
lista_palavra_final = []
let_num = False
prox_letra = ''
lista_completa = ''
print_final = [] 
msg_final = ''
# palavra_final_bool = False
# soma_par_bool = False
# soma_impar_bool = False
# produto_bool = False
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#resolver problema dos espaços entre os inputs
for i in range(total_palavras): #recebe palavra decodificadora e palavra codificada:
    palavra_codificada = []
    palavra_decodificadora = []
    palavra_codificada_sem_carac_especial = []
    resposta = []
    input()
    palavra_decodificadora = str(input())
    input()


    if palavra_decodificadora == 'Portal': # ok    palavra_codificada = input().split(' ')
        palavra_codificada = input().split(' ')
        for i in palavra_codificada:
            if i != '!' and i != '@' and i != '$' and i != '%' and i != '&' and i != '#' and i != ' ':
                palavra_codificada_sem_carac_especial.append(i)
            if len(palavra_codificada_sem_carac_especial) != 0:
              let_num = True

        for j in palavra_codificada_sem_carac_especial:
            if j in alfabeto:
                indice_j = alfabeto.index(j)
                indice_proximaletra = indice_j + 1
                # print(z)
                prox_letra = alfabeto[indice_proximaletra]
                resposta.append(prox_letra)
                # palavra_codificada_sem_carac_especial.insert(palavra_codificada_sem_carac_especial.index(j), alfabeto[indice_proximaletra])
                # palavra_codificada_sem_carac_especial.remove(j)
        palavra_final = ''.join(resposta)
        print_final.append(palavra_final)
        # print(palavra_final)
        
        


    elif palavra_decodificadora == 'Experimento': # ok
        palavra_codificada = input().split(' ')
        for i in palavra_codificada:
            if i != '!' and i != '@' and i != '$' and i != '%' and i != '&' and i != '#' and i != ' ' and i != '':
                palavra_codificada_sem_carac_especial.append(i)
            if len(palavra_codificada_sem_carac_especial) != 0:
              let_num = True
        for j in palavra_codificada_sem_carac_especial:
            if j not in alfabeto: 
                int_j = int(j)
            if int_j%2 == 0:
                par.append(int_j)
        soma_par = sum(par)
        soma_par_str = str(soma_par)
        print_final.append(soma_par_str)
        # print(soma_par)
    



    elif palavra_decodificadora == 'Realidade': # ok
        palavra_codificada = input().split(' ')
        for i in palavra_codificada:
            if i != '!' and i != '@' and i != '$' and i != '%' and i != '&' and i != '#' and i != ' ' and i != '':
                palavra_codificada_sem_carac_especial.append(i)
        if len(palavra_codificada_sem_carac_especial) != 0:
              let_num = True
        for j in palavra_codificada_sem_carac_especial:
            if j not in alfabeto:
                int_j = int(j)
                if int_j%2 == 1:
                    impar.append(int_j)
        soma_impar = sum(impar)
        soma_impar_str = str(soma_impar)
        print_final.append(soma_impar_str)
        # print(soma_impar)


    elif palavra_decodificadora == 'Schembulock': # ok
      produto = 1
      palavra_codificada = input().split(' ')
      

      for i in palavra_codificada:
          if i != '!' and i != '@' and i != '$' and i != '%' and i != '&' and i != '#' and i != ' ':
              palavra_codificada_sem_carac_especial.append(i)
          if len(palavra_codificada_sem_carac_especial) != 0:
            let_num = True
      for j in palavra_codificada_sem_carac_especial:
          if j not in alfabeto:
              j_int = int(j)
              produto *= j_int
      produto_str = str(produto)
      print_final.append(produto_str)
        # print(produto)
  
if let_num: 
  msg_final = ' '.join(print_final)
  print(f'Consegui! A mensagem decodificada de Bill Cipher é: {msg_final}')
else:
  print("Esse formato de mensagem nem Bill Cipher entenderia!")
        


  





