palavra=input("Digite uma palvra qualquer: ")
vogais=['A','E','I','O','U']
consoantes=[]
i=0
while i <len(palavra):
    if palavra[i] not in vogais:
        consoantes.append(palavra[i])
        i=i+1
    else:
        i=i+1
print("LISTA DE CONSOANTES ", consoantes)
print("QUANTIDADE DE CONSOANTES ", len(consoantes))