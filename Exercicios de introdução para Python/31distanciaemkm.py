#Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um 
#percurso, calcule o consumo em Km/l E ESCREVA SE FOR MENOR QUE 8 VENDA \ENTRE 8 E 12 ECONOMICO E MAIOR QUE 12 SUPERECONOMICO
kmrodado=float(input("Digite a distância percorrida: "))
qntdlitro=float(input("Digite a quantidade de combustível consumida: "))
media=kmrodado/qntdlitro
if(media<8):
    print(f"Venda o carro!")
elif(media>=8 and media<=12):
    print(f"Seu carro está econômico!")
else:
    print(f"Seu carro está super econômico! ")
    