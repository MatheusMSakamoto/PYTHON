#FAÇA UM ALGORITMO QUE RECEBA 10 NOMES EM UMA LISTA E AO FINAL APRESENTE TODOS OS NOMES RECEBIDOS
lista_nome=[]
while(len(lista_nome))<10:
    nome=input("Digite um nome: ")
    lista_nome.append(nome)
print(lista_nome)
