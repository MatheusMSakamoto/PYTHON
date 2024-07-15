programa {
  funcao inicio() {
    real saque, conta, sobra
    escreva("Bem vindo ao saque teu dinheiro \n")
    escreva("Digite o quanto voce quer sacar: ")
    leia(saque)
    conta = 1000.00
    se(saque<1000){
      escreva("Você possui saldo \n")
      escreva("\n Você retirou: ", saque, "$")
      sobra = 1000 - saque
      escreva("\nVoce possui na sua conta restantes: ", sobra, "$")
    }
    senao{
      escreva("Você não possui saldo! \n")
      escreva("Você possui ", conta, " $ de saldo")
    }
  }
}
