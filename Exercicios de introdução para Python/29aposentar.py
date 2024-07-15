#LEIA O TEMPO DE SERVIÇO E A IDADE DO TRABALHADOR PARA SABER SE ELE JA PODE APOSENTAR
#TER 65 ANOS ' TER TRABALHADO MIN 30 ANOS OU TER PELO MENOS 60 ANOS E TRALHADOS PELO MENOS 25
idade=int(input("Digite a sua idade: "))
tempo=float(input("Digite quantos anos de serviço você tem: "))
if(idade>=65 or tempo>=25) or (idade==60 and tempo==25):
    print(f"Você está apto a aposentar-se.")
else:
    print(f"Você não está apto a aposentar-se.")