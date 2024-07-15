#VERIFIQUE 3 VALORES SE ELES PODEM SER LADOS DE UM TRIANGULO.SE FOREM É ESCALENO,EQUILATERO OU ISOSCELE
a=float(input("Digite o primeiro valor: "))
b=float(input("digite o segundo valor: "))
c=float(input("Digite o terceiro valor: "))
if(a<(b+c))and(b<(a+c))and(c<(a+b)):
    if(a==b and a==c):
        print("É um triângulo equilátero")
    elif(a==b and a>c or a<c) and (b==c and b>a or b<a):
        print("É um triângulo isósceles")
    elif(a!=b!=c):
        print("É um triângulo escaleno.")