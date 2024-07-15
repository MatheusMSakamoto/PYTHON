def consumo(distancia,litros):
    cons = distancia/litros
    if cons < 8:
        print("Gasta muito!")
    elif cons >= 8 and cons <= 15:
        print("Econômico!")
    elif cons > 15:
        print("Super econômico!")

distancia = float(input("Digite os Km percorridos: "))
litros = float(input("Digite o consumo de combustível gasto no percurso: "))

consumo(distancia,litros)