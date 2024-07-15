#CRIE UM PROGRAMA QUE RECEBA A FELICIDADE E IMPRIMA A POSIÇÃO DE CADA LETRA DA PALAVRA E INFORME QUAL A LETRA ESTÁ SENDO IMPRIMIDA EM X 
#APÓS IMPRIMA QUE O PROGRAMA FOI FINALIZADO

lista= "FELICIDADE"
i=0
while i < len(lista):
    print(f"Posição {i} da letra {lista[i]}")
    i=i+1
print("Progama finalizado.")

#EXEMPLO DOIS

palavra = "FELICIDADE"
for letra in palavra:
    print(letra)
