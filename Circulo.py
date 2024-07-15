#  5 - Classe Círculo: crie uma classe que represente um círculo. Esta classe deve possuir o seguinte atributo:​

# # raio​

# A classe deve ter os seguintes métodos:​

# imprimir o valor do raio;​

# calcular a área do círculo;​

# calcular a circunferência do círculo.​





class Circulo():
    def __init__(self,raio):
        self.raio= raio


    def get_Raio(self):
        print(F"O Raio tem o valor de {self.raio}")

    def get_area_circulo(self):
        area_circulo= 3.14*(self.raio**2)
        print(f"A área do circulo de raio {self.raio} é {area_circulo}")

    def get_circuferencia_circulo(self):
        circuferencia_circulo= (3.14**2)*self.raio
        print(f"A circufenrência do circulo de raio de {self.raio} é {circuferencia_circulo}")




raio= float(input(f"Digite o valor do raio do circulo: "))



Circulo_1= Circulo(raio)

Circulo_1.get_Raio()
Circulo_1.get_area_circulo()
Circulo_1.get_circuferencia_circulo()