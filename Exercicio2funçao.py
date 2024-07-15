#Faça uma função que receba a data atual (dia, mês e ano) e exiba-a na tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000
def data_por_extenso(dia, mes, ano):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    dia = int(dia)
    mes_texto = meses.get(mes)
    if mes_texto:
        print(f"{dia} de {mes_texto} de {ano}")
    else:
        print("Mês inválido")

data_por_extenso(3, 7, 2024)

#------------------------------------------------------------------------------------
