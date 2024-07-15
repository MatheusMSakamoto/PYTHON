# 11 - Classe Transporte: Você deve analisar a hierarquia do transporte tipo Terrestre e da Classe automóvel para criar as subclasses dos tipos de transporte Aéreo e Aquático. Instancie 3 objetos de cada classe e faça os testes nos atributos e métodos específicos de cada subclasse;​
# Crie duas subclasses de Aquático e Aéreo, exemplo:​Lancha e Navio;​AviaoMonomotor e AviaoComercial;​
# Verifique os atributos e métodos específicos de cada subclasse.​
# Superclasse Transporte
class Transporte:
    def __init__(self, nome, capacidade, velocidade):
        self.nome = nome
        self.capacidade = capacidade
        self.velocidade = velocidade
    
    def mostrar_detalhes(self):
        print(f"Nome: {self.nome}, Capacidade: {self.capacidade}, Velocidade: {self.velocidade} km/h")

class Terrestre(Transporte):
    def __init__(self, nome, capacidade, velocidade, numero_rodas):
        super().__init__(nome, capacidade, velocidade)
        self.numero_rodas = numero_rodas
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Número de Rodas: {self.numero_rodas}")

class Aereo(Transporte):
    def __init__(self, nome, capacidade, velocidade, autonomia_voo):
        super().__init__(nome, capacidade, velocidade)
        self.autonomia_voo = autonomia_voo
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Autonomia de Voo: {self.autonomia_voo} horas")

class Aquatico(Transporte):
    def __init__(self, nome, capacidade, velocidade, tipo_propelente):
        super().__init__(nome, capacidade, velocidade)
        self.tipo_propelente = tipo_propelente
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Tipo de Propulsão: {self.tipo_propelente}")

class AviaoMonomotor(Aereo):
    def __init__(self, nome, capacidade, velocidade, autonomia_voo, modelo_motor):
        super().__init__(nome, capacidade, velocidade, autonomia_voo)
        self.modelo_motor = modelo_motor
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Modelo do Motor: {self.modelo_motor}")

class AviaoComercial(Aereo):
    def __init__(self, nome, capacidade, velocidade, autonomia_voo, companhia_aerea):
        super().__init__(nome, capacidade, velocidade, autonomia_voo)
        self.companhia_aerea = companhia_aerea
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Companhia Aérea: {self.companhia_aerea}")

class Lancha(Aquatico):
    def __init__(self, nome, capacidade, velocidade, tipo_propelente, comprimento):
        super().__init__(nome, capacidade, velocidade, tipo_propelente)
        self.comprimento = comprimento
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Comprimento: {self.comprimento} metros")

class Navio(Aquatico):
    def __init__(self, nome, capacidade, velocidade, tipo_propelente, tonelagem):
        super().__init__(nome, capacidade, velocidade, tipo_propelente)
        self.tonelagem = tonelagem
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Tonelagem: {self.tonelagem} toneladas")

carro = Terrestre("Carro", 5, 180, 4)
moto = Terrestre("Moto", 2, 200, 2)

monomotor = AviaoMonomotor("Cessna 172", 4, 226, 8, "Lycoming IO-360-L2A")
comercial = AviaoComercial("Boeing 737", 189, 876, 7, "American Airlines")

lancha = Lancha("Lancha Rápida", 8, 90, "Motor de popa", 7)
navio_carga = Navio("Navio de Carga", 20000, 40, "Motor diesel", 150000)

print("\n=== Transporte Terrestre ===")
carro.mostrar_detalhes()
moto.mostrar_detalhes()
print("\n=== Transporte Aéreo ===")
monomotor.mostrar_detalhes()
comercial.mostrar_detalhes()
print("\n=== Transporte Aquático ===")
lancha.mostrar_detalhes()
navio_carga.mostrar_detalhes()