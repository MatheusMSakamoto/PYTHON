# Crie uma função que retorne uma lista com valor padrão. Para esta função, consideramos como argumentos de entrada a quantidades de elementos 
# e o valor padrão atribuido a todos eles. Exemplo de retorno:
# [1,1,1,1,1,1,1,]
# ["A","A","A","A","A"]





def lista (valor_atribuido, quantidade_de_elementos):
    lista_padrão= [valor_atribuido] * quantidade_de_elementos
    return lista_padrão


print(lista(5,3))
