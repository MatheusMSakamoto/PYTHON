#MEDIA PONDERADA DE 3 PROVAS , A 1 E 2 PESO 1 E A 3 PESO 2 , MOSTRAR MEDIA DO ALUNO SE FOI APROVADO OU REPROVADO . DEVE SER MAIOR OU IGUAL A 60
nota1=float(input("Digite a primeira nota: "))
p1=float(input("Digite o peso da nota: "))
nota2=float(input("Digite a segunda nota: "))
p2=float(input("Digite o peso da nota: "))
nota3=float(input("Digite a terceira nota: "))
p3=float(input("Digite o peso da nota: "))
media=(nota1*p1 + nota2*p2 + nota3*p3)/ (p1+p2+p3)
if(media>=6.0):
    print(f"Você foi aprovado com a média {media}")
else:
    print(f"Você foi reprovado! Sua média é {media}")

