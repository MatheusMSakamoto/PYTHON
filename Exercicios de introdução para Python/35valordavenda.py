#ESCREVA UM PROGRAMA DADO O VALOR DA VENDA IMPRIMA O VALOR DA COMISSÃO
vendamensal=float(input("Digite o valor do faturamento: "))
if(vendamensal>=100000):
    comissao=700 + (vendamensal*(14/100))
    print(f"O Valor de sua comissão será de R${comissao}")
elif(vendamensal<100000 and vendamensal>=80000):
    comissao=650 + (vendamensal*(14/100))
    print(f" O valor de sua comissão será de R${comissao}")
elif(vendamensal<80000 and vendamensal>=60000):
    comissao=600 + (vendamensal*(14/100))
    print(f" O valor de sua comissão será de R${comissao}")
elif(vendamensal<60000 and vendamensal>=40000):
    comissao=550 + (vendamensal*(14/100))
    print(f" O valor de sua comissão será de R${comissao}")
elif(vendamensal<40000 and vendamensal>=20000):
    comissao=500 + (vendamensal*(14/100))
    print(f" O valor de sua comissão será de R${comissao}")
elif(vendamensal<20000):
    comissao=400 + (vendamensal*(14/100))
    print(f" O valor de sua comissão será de R${comissao}")
