#como descobrir todos os shoppings
email_gerente={
    'asuhusa':'shuhausda'

}
#forma 1 
for shopping in email_gerente:
    print(shopping)
#forma 2 usando dicionario.keys()
print(email_gerente.keys())
#-----------------------------------------------------------------------
#No dicionário as posições são descritas pelo nome da chave (ex: 'leblon')
#como verificar se um shopping existe:
if "Iguatemi" in email_gerente:
    print("Tem sim")
else:
    print("Tem não")
#-----------------------------------------------------------------------
