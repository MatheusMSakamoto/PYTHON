programa {
  funcao inicio() {
    real caneta, canetas, valor, gasto, sobra
    escreva("Bem vindo ao calcule o valor! \n")
    escreva ("Digite o quanto vocÊ tem para gastar: ")
    leia(gasto)
    escreva("Digite o quanto de canetas você quer comprar: ")
    leia(canetas)
    caneta = (canetas*1.1)
    sobra = gasto-caneta
    escreva ("Sobrou ", sobra, "$ \n")
    escreva ("Cada caneta custou 1.10$")
      }
}
