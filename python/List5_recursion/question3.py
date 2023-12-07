def Comprimirfrase(frase, contador):
    if len(frase)==0:
      return None
    if len(frase) == 1:
      lista.append(str(contador)+frase[0])
      return None 
    else:
        if frase[0] == frase[1]:
            contador += 1
            if len(frase)==2:
                lista.append(str(contador)+ frase[0])
                frase.remove(frase[0])
                frase.remove(frase[0])
            else:
              frase.remove(frase[0])
            return Comprimirfrase(frase, contador)
        else:
            lista.append(str(contador) + frase[0])
            contador = 1
            frase.remove(frase[0])
            return Comprimirfrase(frase, contador)
        
def RespostaChatGPT(soma):
  if soma<=5:
    resposta="1t3a1 1f1a1c3i1n1h1o1 1n3e"
  elif soma<=20:
    resposta="1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o"
  elif soma<=30:
    resposta="1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a"
  elif soma<=40:
    resposta="1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z"
  else:
    resposta="3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r"
  return resposta
    
def Descomprimir(RespostasChatGPT):
   if len(RespostasChatGPT)==0:
      return None
   else:
      descompressao.append(int(RespostasChatGPT[0])*RespostasChatGPT[1])
      del RespostasChatGPT[1]
      del RespostasChatGPT[0] 
      return Descomprimir(RespostasChatGPT)
      
algarismos=["1","2","3","4","5","6","7","8","9"]   
PrecisoParar=False
TemTraducao=False

while not PrecisoParar:
   comando=input()
   if comando=="Vou pedir ajuda pro meu amigo ChatGPT":
      entender=True
      while entender:
         frases=input()
         if frases=="Não tô entendendo nada":
            entender=False
         else:
            TemTraducao=True
            lista=[]
            lista_soma=[]
            frase_lista=[]
            contador=1
            for i in frases:
               frase_lista.append(i)
            Comprimirfrase(frase_lista, contador)
            frasebonita="".join(lista)
            for j in frasebonita:
              if j in algarismos:
                lista_soma.append(int(j))
            soma=sum(lista_soma)
            respostagpt= RespostaChatGPT(soma)
            print(f"usuário:{frasebonita}")
            print(f"ChatGPT:{respostagpt}")
   elif comando=="Qual era a tradução?":
      if TemTraducao:
         descompressao=[]
         lista_gpt=[]
         for i in respostagpt:
            lista_gpt.append(i)
         Descomprimir(lista_gpt)
         respostabonita="".join(descompressao)
         print(f"Descobri! É: {respostabonita}, tá de brincadeira né?")
      else:
         print("Não tem nada pra traduzir")
   elif comando=="Preciso parar de usar o ChatGPT":
      PrecisoParar=True