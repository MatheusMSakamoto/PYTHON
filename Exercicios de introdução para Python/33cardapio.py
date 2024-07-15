#CRIE UM PROGRAMA QUE LEIA O CÓDIGO E A QUANTIDADE CORRESPONDENTE AO PEDIDO / CALCULE O VALOR A SER PAGO
codlanche=int(input("Digite o código do lanche: "))
qntd=int(input("Digite a quantidade: "))
if(codlanche==100):
    preço=qntd*1.20
    print(f"O Valor do pedido é de R${preço}")
elif(codlanche==101):
    preço=qntd*1.30
    print(f"O Valor do pedido é de R${preço}")
elif(codlanche==102):
    preço=qntd*1.50
    print(f"O Valor do pedido é de R${preço}")
elif(codlanche==103):
    preço=qntd*1.20
    print(f"O Valor do pedido é de R${preço}")
elif(codlanche==104):
    preço=qntd*17
    print(f"O Valor do pedido é de R${preço}")
elif(codlanche==105):
    preço=qntd*9.50
    print(f"O Valor do pedido é de R${preço}")
elif(codlanche==106):
    preço=qntd*6
    print(f"O Valor do pedido é de R${preço}")
