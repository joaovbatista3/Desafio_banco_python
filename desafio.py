menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$  {valor:.2f}\n"
        
        else:
            print ("operação invalida!")
    
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operação falhou! Saldo insuficiente na conta!")
        
        elif excedeu_limite:
            print ("Operação falhou! Valor excede o limite da conta!")
        
        elif excedeu_saques:
            print ("Operação falhou! Número de saques excedidos!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print ("O valor informado é invalido!")
    
    
    elif opcao == "e":
        print ("\n=========EXTRATO=========")
        print ("Não foram feitas movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("=========================")

    elif opcao == "q":
        break

    else:
        print ("operação invalida, selecione outra opção")


