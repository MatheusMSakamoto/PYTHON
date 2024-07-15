def calcularFinanciamento(valor_veiculo, entrada, taxa_juros, num_parcelas):
    valor_financiado=valor_veiculo-entrada
    taxa_juros_decimal=taxa_juros/100
    valor_totalpago=valor_financiado*(1+taxa_juros_decimal)**num_parcelas
    juros_pagos=valor_totalpago-valor_financiado
    valor_parcela=valor_totalpago/num_parcelas
    