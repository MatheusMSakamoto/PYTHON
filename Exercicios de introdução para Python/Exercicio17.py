def imprimei_media(*args):
    soma= 0
    for i in args:
        soma+=i/i
    return soma


objeto=float(imprimei_media (4.5,8,7,9.5))

print(objeto)
print(type(objeto))




def media(*args):
    if not  args:
        return 0.0
    soma = sum (args)
    quantidade = len(args)
    media =soma /quantidade
    return media

resultado1= media(1.5, 2.5, 3.5)
resultado2= media(100, 20.0, 30.0)
resultado3= media(7.5, 14.5, 21.5, 28.5)


print(f"Media dos argumentos (1.5, 2.5, 3.5): {resultado1:.2f}")
print(f"Media dos argumentos ((100, 20.0, 30.0): {resultado2:.2f}")
print(f"Media dos argumentos (7.5, 14.5, 21.5, 28.5): {resultado3:.2f}")