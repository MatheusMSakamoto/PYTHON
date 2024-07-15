def tansf_seg(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    print(f"Horas totais em segundos = {total_segundos}")

horas = int(input("Digite as horas:"))
minutos = int(input("Digite as minutos:"))
segundos = int(input("Digite as segundos:"))

tansf_seg(horas,minutos,segundos)