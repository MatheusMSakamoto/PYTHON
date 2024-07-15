#PÃO CUSTA 0,12 E BROA CUSTA 1,50 , QUANTO O DONO ARRECADOU COM A VENDA DOS DOIS JUNTOS E GUARDAR 10% EM UMA POUPANÇA
qntdpao=int(input("Quantos pães foram vendidos ao fim do dia? "))
qntdbroa=int(input("Quantas broas foram vendidas ao fim do dia? "))
totalvendido=(qntdpao*0.12)+(qntdbroa*1.5)
poupanca=totalvendido*10/100
print(f"Ao final do dia foram arrecadados R${totalvendido}, o valor para depositar na poupança fica em R${poupanca}")