# Classe Compra: Crie uma super classe que modele uma Venda. Esta classe deve possuir os seguintes atributos:​
# Numero; Produto; Valor; Valor_total = 0;​# Método:​# calcular_valor_total(): deve somar ao valor_total o imposto de 17% do ICMS + o Frete de 5% sobre o valor do protudo;​
# Subclasses:​
# Defina as subclasses Avista e Parcelada, na classe de compra a vista deve ter o atributo desconto e na classe Parcelada numero de parcelas.​
# Em cada subclasse definir um método que retorna o preço com desconto ou o valor das parcelas.​

class Venda:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0
    
    def calcular_valor_total(self):
        icms = 0.17 * self.valor
        frete = 0.05 * self.valor
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class Avista(Venda):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto
    
    def calcular_valor_com_desconto(self):
        valor_total_com_impostos = self.calcular_valor_total()
        valor_com_desconto = valor_total_com_impostos * (1 - self.desconto / 100)
        return valor_com_desconto

class Parcelada(Venda):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas
    
    def calcular_valor_parcela(self):
        valor_total_com_impostos = self.calcular_valor_total()
        valor_parcela = valor_total_com_impostos / self.numero_parcelas
        return valor_parcela

venda_avista = Avista(1, "Notebook", 3000.0, 10)
venda_parcelada = Parcelada(2, "Smartphone", 1500.0, 12)

print(f"Valor total da venda à vista com desconto: {venda_avista.calcular_valor_com_desconto():.2f}")
print(f"Valor de cada parcela na venda parcelada: {venda_parcelada.calcular_valor_parcela():.2f}")
