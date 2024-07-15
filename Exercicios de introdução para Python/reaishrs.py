#VALOR DA HORA DE TRABALHO E NUMERO DE HORAS TRABALHADAS
valorhr=float(input("Digite o valor pago pela hora de trabalho: "))
hrtrabalhada=(float(input("Digite quantas horas você trabalhou: ")))
pgmt=valorhr*hrtrabalhada
sal=pgmt*10/100
res=pgmt+sal
print(f"O Valor a ser recebido com o aumento é R${res}")
