def calcularTempo(hr_minuto):
    pis = 0.0033
    cofins = 0.002
    icms = 0.17
    valor_min_porhora=9.00
    valor_adicionalhr=1.50
    hrs_completas=hr_minuto/60
    min_restantes=hr_minuto%60
    if hr_minuto <=15:
        return 0.00
   
    if min_restantes > 0:
        hrs_completas +=1

    if hrs_completas ==1:
        total=valor_min_porhora
    else:
        total=valor_min_porhora + (hrs_completas -1) * valor_adicionalhr
        total = total+pis+cofins+icms
        return total
tempo_utilizado=int(input("Digite o tempo utilizado no estacionamento: "))
valorfinal= calcularTempo(tempo_utilizado)
print(f"O Valor total a ser pago será de R${valorfinal:.2f}")