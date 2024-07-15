def inverso(num):
    num_str = str(num)           
    num_list = list(num_str)    
    num_list.reverse()           
    num_reverso_str = "".join(num_list)  
    num_reverso = int(num_reverso_str)  
    print(f"Número invertido é: {num_reverso}")

x = int(input("Digite o número: "))
inverso(x)