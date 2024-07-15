#DETERMINE SE O ANO LIDO É BISEXTO\ PARA SER BISEXTO TEM QUE SER DIVISIVEL POR 400 OU POR 4 E NAO POR 100
ano=int(input("Digite o ano: "))
res=(ano%4)
if(res==0):
    print(f"O Ano é bissexto.")
else:
    print(f"O Ano não é bissexto. ")