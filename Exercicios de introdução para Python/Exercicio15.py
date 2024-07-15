# função "*args" e "**kwargs"


# args(cria valores e salva em tuplas)

def imprimei_nome(nome1, nome2, *args):
    
    return nome1, nome2, args


objeto= imprimei_nome("Fabio", "Jonas", "Leandro", "Roberto", "Rafael")
print(objeto)
print(type(objeto))

print("="*100)
# kwargs(cria valores e salva em tuplas)

def imprime_nome_2(**kwargs):

    return kwargs

objeto= imprime_nome_2(nome1="Jose", nome2= "Rafael", nome3= "Leandro" )
print(objeto)
print(type(objeto))