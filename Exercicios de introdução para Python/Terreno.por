programa {
  funcao inicio() {
    real area, base, altura, preco

    escreva("Bem vindo ao calcule a area do terreno \n")
    escreva("Digite a base do terreno: ")
    leia(base)
    escreva("Digite a altura do terreno: ")
    leia(altura)
    area = base*altura
    preco = area*750.00
    escreva("Calculando.. \n")
    escreva("\n")
    escreva("O preço deste terreno é: $", preco, ",00 reais. \n")
    escreva("\n")
    escreva("Obrigado por utilizar o programa.")
      }
}
