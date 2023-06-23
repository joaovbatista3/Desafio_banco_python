def menu(): 
    menu ="""

    [d] depositar
    [s] sacar
    [e] extrato
    [nc] nova conta
    [lc] listar contas
    [nu] novo usuário
    [q] sair

    => escolha uma opção: """
    return input(menu)

def depositar (saldo, valor, extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$  {valor:.2f}\n"
        
    else:
            print ("operação invalida!")

    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
    
    return saldo,extrato

def exibir_extrato (saldo,/,*, extrato):
    print ("\n=========EXTRATO=========")
    print ("Não foram feitas movimentações." if not extrato else extrato)
    print (f"\n Saldo: R$ {saldo:.2f}")
    print ("=========================")

def criar_usuario (usuarios):
      cpf = input ("Informe o número de CPF: ")
      usuario = filtrar_usuario (cpf,usuarios)

      if usuario:
            print("Este usuário já existe!")
            return
      
      nome = input("Informe seu nome: ")
      data_nascimento = input("Informe sua data de nascimento: ")
      endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

      usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

      print("Usuário criado com sucesso!")

def filtrar_usuario (cpf,usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
      return usuarios_filtrados [0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
      cpf = input ("Informe o CPF do usuário: ")
      usuario = filtrar_usuario (cpf,usuarios)

      if usuario:
            print (" Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta":numero_conta,"usuario":usuario}
      
      print ("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)
      

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"  

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("informe o valor do deposito: "))

            saldo, extrato = depositar(saldo,valor,extrato)

    
        elif opcao == "s":
            valor = float(input("informe o valor do saque: "))

            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
              exibir_extrato(saldo,extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print ("operação invalida, selecione outra opção")


main()
