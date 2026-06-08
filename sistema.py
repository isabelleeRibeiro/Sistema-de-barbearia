clientes = []
quantidade = int(input("Qual a quantidade de clientes?: "))
qnt_servicos = 0
total_faturado = 0
num = 0

for i in range(quantidade):
        nome = input(f"Qual o nome do {i+1}° cliente?")
        clientes.append(nome)
        
        if i == quantidade-1:
            print("\n Fila:")
            for fila in clientes:
                num = num + 1
                print(f"{num}° da fila - {fila}")
    

for a in range(quantidade):
    
    valor_total = 0
    
    while True:
        
        print("\n1- Cabelo, R$20")
        print("2- Bigode, R$10")
        print("3- Barba, R$15")
        print("4- Finalizar serviço.")
        servico = int(input(f"Selecione os serviços que o cliente {clientes[a]} deseja:"))
        if servico < 1 or servico > 4:
            print("Opção inválida, retorne ao menu.")
        else:
            if servico == 1:
                valor_total = valor_total + 20
                qnt_servicos = qnt_servicos + 1
            elif servico == 2:
                valor_total = valor_total + 10
                qnt_servicos = qnt_servicos + 1
            elif servico == 3:
                valor_total = valor_total + 15
                qnt_servicos = qnt_servicos + 1
            elif servico == 4:
                print(f"Valor total do(s) serviços: R${valor_total}")
                total_faturado += valor_total
                break
            
print(f"\nQuantidade total de servicos prestados: {qnt_servicos} ")
print(f"Valor total faturado: R${total_faturado}")
