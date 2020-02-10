def elSegundo(s,lista):
  frase=list(s)
  nuevaFrase=list(s)
  cantidad=len(lista)/2
  indice=0
  while(indice<=cantidad):
    nuevaFrase[2*indice]=frase[2*indice+1]
    indice=indice+1
  print(nuevaFrase)

listas=[4,0,5,8,11,4]
print("zasca")
elSegundo('tienes dos horas',listas)

