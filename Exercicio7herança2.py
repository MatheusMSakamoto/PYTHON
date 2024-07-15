class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}")

class BuzzLightyear(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele pode voar!")

class Woody(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele pode laçar!")

class MrPotatoHead(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele pode mudar de rosto!")

class Rex(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele é um dinossauro que ruge!")

class SlinkyDog(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele pode esticar!")

class Hamm(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele é um cofrinho que guarda moedas!")

class BoPeep(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ela tem um cajado mágico!")

class Alien(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele vem do espaço!")

class Jessie(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ela é uma vaqueira valente!")

class Forky(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
    def brincar(self):
        print(f"Estou brincando com {self.nome}. Ele é feito de um garfo!")

buzz = BuzzLightyear("Buzz Lightyear", "Branco", "Médio", 120.0)
woody = Woody("Woody", "Marrom", "Médio", 100.0)

buzz.brincar()  
woody.brincar()
