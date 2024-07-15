#empresa de RH 
#SISTEMA SE A PESSOA POSSUI A IDADE MINIMA 18 , PASSA FASE 1 , CURSO DE QUALIFICAÇÃO PASSA FASE 24
#CONHECIMENTOS ESPECIFICOS , SE NOTA FOR MAIOR QUE 7 ESTÁ APTA SENÃO RECEBE EMAIL AGRADECENDO
#SEMPRE QUE PASSAR A FASE RECEBE UM EMAIL DIZENDO PARABENS VOCE PASSOU PARA PROXIMA FASE
cargo=input("Digite o cargo ao qual se inscreveu: ")
nome_completo=input("Digite seu nome completo: ")
email=input("Digite o seu email: ")
idade=int(input("Digite a sua idade: "))
if(idade>=18):
    print("Parabéns, você passou para próxima fase. ")
    curso=input("Digite se voce tem um curso de qualificação: ")
    if(curso=="Sim"):
        print("Parabéns, você passou para prova de conhecimentos! ")
        nota=float(input("Digite o valor de sua nota na prova de conhecimentos: "))
        if(nota>=7):
            print("Parabéns, você está apto a preencher a vaga! ")
        else:
            print("Obrigado por participar do processo seletivo. ")
    else:
        print("Obrigado por participar do processo seletivo! ")
else:
    print("Obrigado por participar do processo seletivo! ")