menu = ('''
[d] Depositar
[s] Sacar
[e] Extrato
[q] SAIR 

--> ''')

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= limite_saque

        if excedeu_saldo:
            print('Operação falhou! Saldo insuficiente.')

        elif excedeu_limite:
            print('Operação falhou!O valor do saque excede o limite.')

        elif excedeu_saque:
            print('Operação falhou! Número máximo de saque excedido.')

        elif valor < saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "e":
        print('\n======== EXTRATO ========')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('===========================')

    elif opcao == 'q':
        print('Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente!')