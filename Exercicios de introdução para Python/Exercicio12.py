def lista(media_lista):
    calc=sum(media_lista)/len(media_lista)
    return calc
lista_media=[]
while len(lista_media) < 10:
    lista_media.append(int(input("Digite um número: ")))
print(f"A média da lista é {lista(lista_media)}")

#----------------------------------------------------------------
def media(lista):
    soma=0
    for num in lista:
        soma+=num
    media=soma/len(lista)
    return media

#-----------------------------------------------------------------
