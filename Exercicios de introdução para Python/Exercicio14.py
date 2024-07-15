def calculaValor(consumo,preco):
    valor=consumo*preco
    return valor 

def calculaConsumo(potencia,hrs, preco):
    consumo=potencia*hrs/1000
    conta=calculaValor(consumo,preco)
    return conta

potencia=int(input("Digite a potencia do aparelho: "))
tempo=int(input("Digite o tempo que foi utilizado: "))
preco=float(input("Digite o valor KWH: "))
banho= calculaConsumo(potencia,tempo,preco)
print("R$:",banho)

