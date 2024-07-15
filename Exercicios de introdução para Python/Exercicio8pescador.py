def calcpescado(qntdpescado,multa):
    multa=4.00
    pesounidade=1
    pesopermitido = 50

    if qntdpescado > 50:
        pesototal = pesounidade*qntdpescado
        excesso = pesototal - pesopermitido
        valormulta = excesso*multa
        return valormulta
    else:
        return ("Peso capturado não ultrapassou o limite permitido")
multa=4.00
qntdpescado=int(input("Digite a quantidade de pescado capturado: "))
res=calcpescado(qntdpescado, multa)
print(f"O limite de peso foi excedido, gerando uma multa de R${res} para o liberamento do pescado.")