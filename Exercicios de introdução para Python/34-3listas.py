lista=[]
par=[]
impar=[]
i=0
while i <20:
    num=int(input("Digite um número: "))
    if num % 2 == 0:
        par.append(num)
        lista.append(num)
        
    else:
        impar.append(num)  
        lista.append(num)
    i=i+1
print(lista)
print(par)
print(impar)
