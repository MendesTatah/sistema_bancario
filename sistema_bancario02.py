def menu():
    menu = ('''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo Usuário
    [q] SAIR 
    --> ''')
    return input(menu)



def depositar(saldo, valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDeposito realizado com sucesso!!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato



def sacar(*, saldo, valor, extrato, limite, numero_saque,limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
        print('Operação falhou! Saldo insuficiente.')

    elif excedeu_limite:
        print('Operação falhou!O valor do saque excede o limite.')

    elif excedeu_saque:
        print('Operação falhou! Número máximo de saque excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saque += 1
        print("\nSaque Realizado com sucesso!!")
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo, extrato



def exibir_extrato(saldo, /, *, extrato):
    print('\n======== EXTRATO ========')
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print('===========================')




def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nUsuário já existe com esse CPF!")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aa): ")
    endereço = input("Informe seu endereço (Logadouro, nº - bairro - Cidade/sigla Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print('Usuário criado com sucesso!!')



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None




def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!Criação de conta encerrado.")



def listar_contas(contas):
    for conta in contas:
        linha = f"""
Agência: {conta["agencia"]}
C/C:{conta["conta"]} 
Titular: {conta['usuario']['nome']}"""
        print("-" * 100)
        print(linha)

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3
usuarios = []
contas = []
agencia = "0001"

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))
        saldo, extrato = sacar(saldo=saldo,
                               valor=valor,
                               extrato=extrato,
                               limite=limite,
                               numero_saque=numero_saque,
                               limite_saque=limite_saque)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == 'q':
        print('Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente!')