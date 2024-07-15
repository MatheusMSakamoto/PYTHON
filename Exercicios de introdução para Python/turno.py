#FAÇA UM PROGRAMA QUE PERGUNTE EM QUE TURNO VOCE ESSTUDA. M- MATUTINO V- VEPERTINO E N - NOTURNO
#DIGITE BOM DIA BOA TARDE BOA NOITE OU VALOR INVALIDO
turno=input("Digite o seu turno, v para vespertino, m para matutino ou n para noturno: ")
if(turno=="v"):
    print("Boa tarde!")
elif(turno=="m"):
    print("Bom dia!")
elif(turno=="n"):
    print("Boa noite")
else:
    print("Valor inválido.")
    