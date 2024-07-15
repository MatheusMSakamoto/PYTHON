# 5 - Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:​
# Nome; Telefone; E-mail; Endereço;​# Métodos:# negociar: deve printar uma mensagem de negociação;​
# Subclasses:​
# Defina as subclasses de Pessoa serão Física e Jurídica, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: CPF, CNPJ.​
# Além de herdar o método negociar() crie métodos específicos para as subclasses;​

class Humano():
    def __init__(self,nome,telefone,email,endereco):
        self.nome= nome
        self.telefone= telefone
        self.email= email
        self.endereco= endereco
    
    def Negociar(self):
        print(f"Negocianção Iniciada...")

class HumanoFisico(Humano):
    def __init__(self, nome, telefone, email, endereco,cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf= cpf

    def getCPF(self):
        print(self.cpf)
    
    def setCPF(self,novo_cpf):
        self.cpf= novo_cpf
        return self.cpf
    
class HumanoJuridica(Humano):
    def __init__(self, nome, telefone, email, endereco,cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj= cnpj

    def getCNPJ(self):
        print(self.cnpj)
    
    def setCNPJ(self,novo_cnpj):
        self.cnpj= novo_cnpj
        return self.cnpj
    
pessoa1= HumanoFisico("Rafael",991924837,"rafa.rodriques12@gmail.com","Rua Venancio Aires,353",10412847132)
pessoa2= HumanoJuridica("Rafael",991924837,"rafa.rodriques12@gmail.com","Rua Venancio Aires,353",87654387654)

pessoa1.getCPF()
pessoa1.setCPF(876545432)
pessoa1.getCPF()
print("="*100)
pessoa2.getCNPJ()
pessoa2.setCNPJ(1234567)
pessoa2.getCNPJ()