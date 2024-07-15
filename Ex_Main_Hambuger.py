from Hamburger import Hambuerger


codigo=int(input("Digite o código do Produto: "))
preco=float(input("Digite o preco do Produto: "))

lista= {'Bancon', 'Pão', 'Salada', 'Cheddr', 'Double Buger', 'Cebola Caramelizada'}

xbacon= Hambuerger(codigo,preco,lista)

preco= xbacon.getPreco()
print(f"Preco Xbacon: {preco}")

xbacon.getIngredientes()

xbacon.setPreco(99.90)

print(xbacon.preco)