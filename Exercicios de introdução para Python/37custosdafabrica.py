#LEIA OS CUSTOS DA FABRICA E ESCREVA O CUSTO AO CONSUMIDOR
fabrica=float(input("Digite o custo da fabrica:"))
distribuidor=float(input("Digite a porcentagem de distribuidor: "))
if(fabrica<=12000):
    valor=fabrica+(fabrica*(5/100))
    print(f"O Valor é de R${valor}")
elif(fabrica>12000 and fabrica<=25000):
    valor=fabrica+(fabrica*(10/100))+(fabrica*(15/100))
    print(f"O valor é de R${valor}")
elif(fabrica>25000):
    valor=fabrica+(fabrica*(15/100))+(fabrica*(20/100))
    print(f"O valor é de R${valor}")

