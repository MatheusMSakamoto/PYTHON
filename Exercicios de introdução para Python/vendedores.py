#CRIE UM PROGRAMA PARA AUXILIAR OS VENDEDORES NA TABELA DE PREÇOS
valor=(float(input("Digite o valor que deseja consultar: ")))
vdesc=valor - (valor*10/100)
vparc=valor/3
comissaocash=vdesc*5/100
comissaocredt=valor*5/100
print(f"O Valor a ser pago a vista é R${vdesc}\nO valor da parcela em 3x é R${vparc}\nA comissão a vista é R${comissaocash}\nA comissão a prazo é R${comissaocredt}")
