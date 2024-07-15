#FABRICA DE CAMISETAS, PEQUENO 35,MEDIO 45,GRANDE 55,
camp=int(input("Digite a quantidade de camisetas TAM P vendidas: "))
valorp=camp*35.00
camm=int(input("Digite a quantidade de camisetas TAM M vendidas: "))
valorm=camm*45.00
camg=int(input("Digite a quantidade de camisetas TAM G vendidas: "))
valorg=camg*55.00
valort=valorp+valorm+valorg
print(f"O Valor das vendas por categoria é:\nCAMISETAS P: R${valorp}\nCAMISETAS M: R${valorm}\nCAMISETAS G: R${valorg}\nTOTAL DAS VENDAS: R${valort}")