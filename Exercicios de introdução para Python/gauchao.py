#LANCHONETE GAUCHAO
quantidadesanduiche=int(input("Digite a quantidade de sainduiches: "))
hamburguer=100
conversaohambuguer=hamburguer/1000
queijo=50
conversaoqueijo=queijo/1000
presunto=50
conversaopresunto=queijo/1000
sanduichequeijo=(2*conversaoqueijo)*quantidadesanduiche
sanduichepresunto=(1*conversaopresunto)*quantidadesanduiche
sanduichehamburguer=(1*conversaohambuguer)*quantidadesanduiche
print(f"Você terá de comprar {sanduichequeijo}KG de queijo, {sanduichepresunto}KG de presunto e {sanduichehamburguer}KG de carne.")
