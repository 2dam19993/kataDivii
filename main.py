def elSegundo(s,lista):
  frase=list(s)
  nuevaFrase=list(s)
  cantidad=len(lista)
  indice=0
  while(indice<cantidad):
    print(indice)
    print(cantidad)
    print(len(frase))
    print(nuevaFrase[lista[indice]])
    print(frase[lista[cantidad-indice-1]])
    nuevaFrase[lista[indice]]=frase[lista[cantidad-indice-1]]
    indice=indice+1
  print(nuevaFrase)

listas=[4,0,5,8,11,4]
print("zasca")
elSegundo('tienes dos horas',listas)
