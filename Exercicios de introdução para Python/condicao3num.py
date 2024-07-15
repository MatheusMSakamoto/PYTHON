#RECEBA 3 NUM E COLOQUE EM ORDEM CRESCENTE print(sorted(num1,num2,num3)) comando de ordem
num1=int(input("Digite um número:"))
num2=int(input("Digite outro número: "))
num3=int(input("Digite mais um número: "))
if(num1<num2 and num1<num3):
    print(f"{num1}")
    if(num2<num3):
        print(f"{num2}")
        print(f"{num3}")
    else:
        print(f"{num3}")
        print(f"{num2}")
elif(num2<num1 and num2<num3):
    print(f"{num2}")
    if(num1<num3):
        print(f"{num1}")
        print(f"{num3}")
    else:
        print(f"{num3}")
        print(f"{num1}")
elif(num3<num2 and num3<num1):
    print(f"{num3}")
    if(num1<num2):
        print(f"{num1}")
        print(f"{num2}")
    else:
        print(f"{num2}")
        print(f"{num1}")