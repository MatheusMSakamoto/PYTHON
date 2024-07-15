#RECEBA O SALARIO BASE  CALCULE E IMPRIMA O SALARIO COM GRATIFICAÇÃO DE 5% E PAGA 7% DE IMPOSTO
salariobase=(float(input("Digite o valor do salário base: ")))
grtf= salariobase*5/100
impst= salariobase*7/100
salariog=salariobase+grtf
res=salariog-impst
print(f"\n O salário liquido fica no valor de R${res}, tendo sido o valor de R${grtf} de gratificação e R${impst} abatido do imposto.")