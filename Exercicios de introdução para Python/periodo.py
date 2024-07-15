#BRECHO \ SE O PREÇO É MENOR QUE 50 DE AQUISIÇÃO O VALOR COMERCIALIZADO SERÁ 45%
#CASO SEJA ACIMA O LUCRO SERÁ DE 30%
produto=float(input("Digite o valor do produto: "))
prodfinal= produto * (45/100)
prodfinal2= produto * (30/100)
valorfinal=produto + prodfinal
valorfinal2=produto + prodfinal2
if(produto < 50):
    print(f"O valor de comercio deste produto será de R${valorfinal}")
elif(produto>=50):
    print(f"O valor de comercio deste produto será de R${valorfinal2}")
