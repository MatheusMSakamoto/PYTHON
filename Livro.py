
# 2 - Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:​

# Nome​

# Autor​

# Editora​

# Páginas​

# A classe deve ter o seguintes métodos:​

# Alterar_editora()​

# Listar_qtde_paginas()​




class Livro:
    def __init__(self, nome,autor,editora,paginas):
        self.nome= nome
        self.autor= autor
        self.editora=editora
        self.paginas=paginas

    
    def Set_Editora(self, nova_editora):
        self.editora= nova_editora


    def Get_Quant_Paginas(self):
        for i in range(self.paginas+1):
            x=print(i)




nome_livro= input(f"Digite o nome do livro: ")
nome_autor= input(f"Digite o nome do autor: ")
nome_editora= input(f"Digite o nome da editora: ")
quantidade_paginas= int(input(f"Digite a quantidade de paginas do livro: "))


livro_1= Livro(nome_livro,nome_autor,nome_editora,quantidade_paginas)

print(f"{livro_1.editora}")
print(f"Trocando Editora...")
livro_1.Set_Editora("Martelinho")

print(f"{livro_1.editora}")

livro_1.Get_Quant_Paginas()


