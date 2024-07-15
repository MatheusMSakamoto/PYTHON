#CALCULE TRES NOTAS ATRIBUIDAS ENTRE O INTERVALO DE 0 ATÉ 10
#TRABDELAB PESO 2 , AVASEMESTRAL PESO 3 E EXAMEFINAL PESO5
notatrab=float(input("Digite a nota do trabalho: "))
avanota=float(input("Digite a nota da avaliação: "))
notaexa=float(input("Digite a nota do exame final: "))
media=(notatrab*2 + avanota*3 + notaexa*5)/10
if(media<=2.9):
    print(f"O Aluno está reprovado. sua média é {media}")
elif(media>=3 and media<=5.9):
    print(f"O Aluno está de recuperação. Sua média é {media}")
else:
    print(f"O Aluno está aprovado. Sua média é {media}")