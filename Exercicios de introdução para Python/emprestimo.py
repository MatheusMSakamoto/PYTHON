#EMPRESTIMO AUTOMATICO NO APP \ LEIA O SALARIO DE UM TRABALHADOR E A PRESTAÇÃO DE UM EMPRESTIMO\ SE A PRESTAÇÃO FOR MAIOR QUE 20% IMPRIMA N CONCEDIDO CASO CONTRARIO IMPRIMA CONCEDIDO.
salario=float(input("Digite o valor de seu salário: "))
prestação=float(input("Digite o valor da prestação que deseja pagar: "))
porcentagemsalario=prestação*20/100
valortotal=prestação+porcentagemsalario
if(salario<valortotal):
    print("O Empréstimo não foi concedido.")
else:
    print("O Empréstimo foi concedido.")
