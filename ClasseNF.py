# 10 - Classe NF: Crie uma classe que modele uma Nota_Fiscal. Esta classe deve possuir os seguintes atributos:​

# Numero; Tipo (Entrada/Saída); Série (1,2 ou 3); CNPJ; Razão Social; Data; Valor Produtos; ICMS; Frete; IPI; Valor total;​

# A classe deve ter o seguintes métodos:​

# obterNumero();​

# obterDataEmissão();​

# alterarRazaoSocial();​

# calcularValorTotal() – somar valor do produto + frete e impostos e armazenar na variável valor_total.



class Nota_Fiscal():
    def __init__(self,numero,tipo,serie,CNPJ,razao_social,dia,mes,ano,valor_produtos,ICMS,frete,valor_total=0):
        self.numero=numero
        self.entrada=tipo
        self.serie=serie
        self.CNPJ= CNPJ
        self.razao_social=razao_social
        self.dia= dia
        self.mes= mes
        self.ano=ano
        self.valor_produtos=valor_produtos
        self.ICMS=ICMS
        self.frete= frete
        self.valor_total= valor_total

    def Obter_Numero(self):
        return print(f"Numero da nota fical é {self.numero}")
    
    def Obter_data(self):
        print(f"O dia de hoje é {self.dia}/{self.mes}/{self.ano}")

    def Alterar_Razao_Social(self,nova_razao_social):
        self.razao_social = nova_razao_social
    
    def Calcular_Valor_total(self):
        calculo_icms= (self.ICMS/100)*self.valor_produtos
        calculo_total= self.valor_produtos+self.frete+calculo_icms
        self.valor_total= calculo_total
        return self.valor_total



numero= int(input("Digite o número da nota fiscal: "))
tipo= input("Digite (E) para entrada e (S) para saída da nota fiscal: ")
numero_serie= int(input("Digite o número de serie da nota fiscal: "))
CNPJ= int(input("Digite o CNPJ da empresa da nota fiscal: "))
razao_social= input("Digite a razão social da empresa da nota fiscal: ")
dia= int(input("Digite o dia: "))
mes= int(input("Digite o mês: "))
ano= int(input("Digite o ano: "))
valor_produto= float(input('Digite o valor do produto: '))
ICMS= float(input("Digite o valor em porcentagem do ICMS: "))
frete= float(input("Digite o valor do frete: "))

Nota_Fical_1= Nota_Fiscal(numero,tipo,numero_serie,CNPJ,razao_social,dia,mes,ano,valor_produto,ICMS,frete)
print("="*100)
Nota_Fical_1.Obter_Numero()
print("="*100)
Nota_Fical_1.Obter_data()
print("="*100)
print(Nota_Fical_1.razao_social)
print("="*100)
Nota_Fical_1.Alterar_Razao_Social("Senac Hub")
print(Nota_Fical_1.razao_social)
print("="*100)
print(f"O valor total do produto é {Nota_Fical_1.Calcular_Valor_total()}")