#FABRICA DE REFRIGERANTE LATA 350ML GARRAFA 600ML E GARRAFA 2L 
lata=int(input("Quantas unidades em lata voce recebeu? "))
g600=int(input("Quantas unidades em garrafas de 600ml voce recebeu? "))
g2l=int(input("Quantas unidades em garrafas de 2L voce recebeu? "))
valorlata=350
valorg600=600
valorg2l=1000
qntdlata=(lata*valorlata)/1000
qtndg600=(g600*valorg600)/1000
qntdg2l=(g2l*valorg2l)/1000
qntdtotal=qntdlata+qtndg600+qntdg2l
print(f"A quantidade total recebida em litros é de {qntdtotal} L de refrigerante.")