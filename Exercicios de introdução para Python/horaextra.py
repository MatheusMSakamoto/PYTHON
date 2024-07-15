#HORA TRABALHADA 32,50 E HORA EXTRA 44,50
horat=int(input("Digite as horas trabalhadas: "))
horae=int(input("Digite as horas extras realizadas: "))
valort=horat*32.50
valore=horae*44.50
valortot=valort+valore
valorl=valort*11/100
salario=valortot-valorl
print(f"O Salário bruto será de R${valortot} e o salário líquido será de R${salario}")

