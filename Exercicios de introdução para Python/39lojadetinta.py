#LEIA EM METROS QUADRADOS A AREA A SER PINTADA , COBERTURA DE TINTA É 1 LITRO/6MTS QUADRADOS
#TINTA GALÃO18L CUSTA R$80,00 OU EM GALOES DE 3,6L CUSTA R$25,00
#INFORME A QUANTIDADE DE TINTA A SER COMPRADA E O PREÇO
import math
mts=float(input("Digite o valor da area a ser pintada: "))
valor18l=80
valor3l=25
mtstinta=mts/6
valortotal18=mtstinta*valor18l
valortotal3=mtstinta*valor3l
print(valortotal18,valortotal3)
