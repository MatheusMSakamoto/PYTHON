# 9 - Classe Carro: Crie uma classe que modele um Carro. Esta classe deve possuir os seguintes atributos:​

# Modelo, Marca, Cor, Ano, Valor, Nível (default 0) , Consumo​

# A classe deve ter o seguin tes métodos:​

# abastecer(); - deve incrementar no nível do tanque de combustível.​

# andar(); - recebe a distancia em km que o veículo andou​

# verificar_nível(); - o deve criar uma forma de calcular quantos litros de comb. foram gasto por km​

# calcular_imposto()  -  deve considerar o IPVA do carro em 2,5% do valor.




class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=5):
        self.modelo= modelo
        self.marca=marca
        self.cor=cor
        self.ano= ano
        self.valor=valor
        self.nivel= nivel
    
    def Calcular_Imposto(self):
        imposto = (self.valor*3)/100
        return imposto
    
    def Ligar(self):
        print(f"{self.modelo} Carro ligado")

    def Abastecer(self,qut_litros):
        self.nivel+= qut_litros

    def Andar(self,km):
        consumo= km/10.8
        self.nivel-=consumo
        print

    def Verificar_Nivel(self):
        return self.nivel




car1= Carro("Jetta","Volks","Prata",2022,180000)
    
print(f"Impsoto é de {car1.Calcular_Imposto()} R$")
car1.Ligar()
print(f"Nivel gasolina {car1.nivel}L")
car1.Abastecer(30)
print(f"Nivel gasolina {car1.nivel}L")
car1.Andar(250)
tanque= car1.Verificar_Nivel()
print(f"Tanque = {tanque:.2f}")