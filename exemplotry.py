x=500
y=0
#TENTE REALIZAR A DIVISÃO
try:
    res=x/y
    print(res)
#CASO DÊ ERRO CAI NO EXCEPT > TRATAR A VARIAVEL PARA DAR CERTO
except:
    print("Erro ao tentar realizar a divisâo")
    y=int(input("Digite y novamente: "))
#DEPOIS DE TRATADO FINALIZA O CODIGO
finally:
    res=x/y
    print("RESULTADO: ",res)

#-----------------------------------------------------------

i=0
soma=0
while i <10:
    try:
        x=int(input("Digite um número: "))
        soma+=x
        i+=1
    except:
        print("Valor inválido. Tente novamente")
    
print(soma)
