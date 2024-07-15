#LEIA 2 NOTAS DE UM ALUNO VERIFIQUE SE SÃO VALIDAS (0.0 E 10.0) E IMPRIMA NA TELA A MÉDIA DELAS
nota1=float(input("Digite a sua primeira nota: "))
nota2=float(input("Digite a sua segunda nota: "))
media=(nota1+nota2)/2
if(nota1 >=0.0 and nota1 <=10.0 and nota2 >=0.0 and nota2 <=10.0):
    print(f"A média das notas é : {media}")
else:
    print("As notas não são válidas")
    