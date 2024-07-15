#ESCREVA 10 NUM E ESCREVA O MENOR E MAIOR VALOR LIDO

# n=10
# i=0
# menor = 5
# while i < n:
#     i += int(input("Digite um número: "))
#     if i < menor:
#         print(i)
#     else:
#         print(i)
#     i+=1
# print(max(soma))
# print(min(soma))

num_lista=[]
while(len(num_lista))<10:
    num_lista.append(int(input("Digite um número:")))
print(max(num_lista))
print(min(num_lista))