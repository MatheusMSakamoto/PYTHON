def dados_pessoa(**objeto):
    for i, value in objeto.items():
        print(f"{i} = {value}")
    return objeto
objeto= dados_pessoa(nome= "Rafael", idade="19", cidade="Campo Grande", estado="MS", celular="991924837")

print((type(objeto)))
# print(f"{objeto}")
dados_pessoa()

