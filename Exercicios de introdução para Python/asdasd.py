numeros=[2,3,4,11,5,10,12,18,45]
i=0
while i < len(numeros):
    print(numeros[i])
    if numeros[i]:
        print("Encontramos o número 11!")
        break
    else:
        i=i+1
