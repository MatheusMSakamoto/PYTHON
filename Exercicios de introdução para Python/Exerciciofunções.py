#CRIE UMA FUNÇÃO QUE NECESSITE DE TRÊS ARGUMENTOS, E QUE IMPRIMA O PRODUTO DESSES TRÊS ARGUMENTOS
#1
def div(num1,num2):
    div=num1/num2
    return div

x=div(22,22)
print(x)
#------------------------------------------------------------
#2
def expo(base,expoente):
    expo=base**expoente
    return expo
z=expo(35,2)
print(z)
#-------------------------------------------------------------
#3
def contador(num):
    return(len(str(num)))
num=(15892)
qntd=contador(num)
print(qntd)
#-------------------------------------------------------------
#4
def num(numero):
    if numero > 0:
        return "P"
    else:
        return "N"
numero=float(input("Digite um número: "))
res=num(numero)
print(res)
#-------------------------------------------------------------
