#DIAS TRABALHADOS POR ENCANADOR E IMPRIMA O RESULTADO 
diaria=30
diatrabalhado=(int(input("Quantos diarias foram feitas: ")))
sal=(diatrabalhado*diaria)
res=sal*8/100
abt=sal-res
print(f"\nO resultado com o abate do imposto fica em R${abt}")
