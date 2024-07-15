# 7 - Classe Triangulo: Crie uma classe que modele um triangulo: ​

# 	– Atributos: LadoA, LadoB, LadoC​

# 	– Métodos: calcular Perímetro, getMaiorLado; ​

# Crie instâncias desta classe. Ele deve pedir ao usuário que informe as medidas de um triangulo. 
# Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.




class Triangulo:
    def __init__(self, ladoA,ladoB,ladoC):
        self.ladoA= ladoA
        self.ladoB= ladoB
        self.ladoC= ladoC

    

    def Get_Perimetro(self):
        calculo_perimetro= self.ladoA+self.ladoB+self.ladoC
        print(f"O perimetro desse trinâgulo é {calculo_perimetro}")
    
    def Get_Lado_Maior(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC: #Pode usar a função "Max"=== Max(ladoA,ladoB,ladoc)
            print(f"O maior lado desse triângulo é {self.ladoA}")
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print(F"O maior lado do trinagulo é {self.ladoB}")
        else:
            print(F"O maior lado é {self.ladoC}")



lado_A= float(input("Digite o primeiro lado do triângulo: "))
lado_B= float(input("Digite um segundo número do triângulo: "))
lado_C= float(input("Digite o terceiro núemro do triângulo: "))
triangulo_1= Triangulo(lado_A,lado_B,lado_C)


triangulo_1.Get_Perimetro()
triangulo_1.Get_Lado_Maior()