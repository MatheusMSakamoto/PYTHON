#EMPRESA PAGA R$40,50 A HORA \ SALÁRIO ACIMA DE R$2500 RECOLHE 11% DE IMPOSTO, INFORME O SALARIO LIQUIDO
hrtrabalhada=float(input("Digite o número de horas trabalhadas: "))
imposto=11/100
salariobruto=40.50*hrtrabalhada
if(salariobruto>2500.00):
    valorretirado=salariobruto*imposto
    salarioliquido=salariobruto-valorretirado
    print(f"Seu salário líquido é {salarioliquido}")
else:
    print(salariobruto)
