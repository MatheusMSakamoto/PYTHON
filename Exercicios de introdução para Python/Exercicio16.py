def imprimei_soma(*args):
    soma= 0
    for i in args:
        soma+=i
    return soma


objeto= imprimei_soma(34,56,11,20,34,54)
print(f"A soma dos números é{objeto}")
print(type(objeto))

