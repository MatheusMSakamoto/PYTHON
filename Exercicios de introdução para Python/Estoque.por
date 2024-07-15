programa {
  funcao inicio() {
    inteiro estq, sant, ent, sd
    escreva(" Bem vindo ao calcule o estoque atual de um produto \n")
    escreva("Digite o numero do estoque do produto do seu ultimo mês: ")
    leia(sant)
    escreva("Digite a quantidade do produto que foi comprada este mês: ")
    leia (ent)
    escreva("Digite a quantidade vendida e a utilizada total desse produto: ")
    leia(sd)
    estq = (sant+ent)-sd
    escreva("\nO estoque atual do produto é: ", estq)
    escreva("\n")
    escreva("Obrigado por utilizar a calculadora!")

  }
}
