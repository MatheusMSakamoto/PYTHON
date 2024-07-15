#Crie uma função para realizar o saque de conta corrente. Uma exceção é lançada sempre que o saldo da conta for inferior ao valor sacado.
class SaldoInsuficienteException(Exception):
    pass

saldo = 1000 

while True:
    try:
        valor = float(input("Digite o valor a ser sacado (ou '0' para sair): "))
        if valor == 0:
            print("Operação encerrada.")
            break
        if valor > saldo:
            raise SaldoInsuficienteException(f"Saldo insuficiente. Seu saldo é {saldo}, mas você tentou sacar {valor}.")
        saldo -= valor
        print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
    except SaldoInsuficienteException as e:
        print(e)
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
