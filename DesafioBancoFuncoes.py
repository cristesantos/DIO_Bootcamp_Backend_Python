import textwrap


def menu():
    opcoes = """\n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExibir extrato
    [c]\tCriar conta
    [l]\tListar contas
    [a]\tAdicionar cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(opcoes))


def mostrar_msg(msg, simbolo="#"):
    print(msg.center(60, simbolo))


def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito:\tR$ {valor:.2f}\n"
        mostrar_msg("Depósito concluído com sucesso!", "#")
    else:
        mostrar_msg("Operação falhou! Valor inválido.", "!")


def sacar(conta, valor, limite, numero_saques, limite_saques):
    sem_saldo = valor > conta["saldo"]
    acima_limite = valor > limite
    limite_saques_excedido = numero_saques >= limite_saques

    if sem_saldo:
        mostrar_msg("Operação falhou! Saldo insuficiente.", "!")
    elif acima_limite:
        mostrar_msg("Operação falhou! Saque acima do limite permitido.", "!")
    elif limite_saques_excedido:
        mostrar_msg("Operação falhou! Limite de saques atingido.", "!")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        mostrar_msg("Saque realizado com sucesso!", "#")
    else:
        mostrar_msg("Operação falhou! Valor inválido.", "!")

    return numero_saques


def exibir_extrato(conta):
    print("\n" + f" EXTRATO CONTA {conta['numero']} ".center(60, "="))
    print("Nenhuma movimentação encontrada." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo disponível:\tR$ {conta['saldo']:.2f}")
    print("=" * 60)


def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        mostrar_msg("Já existe cliente com este CPF!", "!")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    clientes.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    mostrar_msg("Cliente cadastrado com sucesso!", "#")


def buscar_cliente(cpf, clientes):
    filtrados = [c for c in clientes if c["cpf"] == cpf]
    return filtrados[0] if filtrados else None


def criar_nova_conta(agencia, numero, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        conta = {"agencia": agencia, "numero": numero, "cliente": cliente, "saldo": 0, "extrato": ""}
        mostrar_msg("Conta criada com sucesso!", "#")
        return conta

    mostrar_msg("Cliente não encontrado. Conta não criada.", "!")


def exibir_contas(lista_contas):
    print("\n" + " CONTAS CADASTRADAS ".center(60, "="))
    for conta in lista_contas:
        info = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero']}
            Titular:\t{conta['cliente']['nome']}
        """
        print(textwrap.dedent(info))
        print("-" * 60)


def selecionar_conta(contas):
    numero = int(input("Informe o número da conta: "))
    conta = next((c for c in contas if c["numero"] == numero), None)
    if not conta:
        mostrar_msg("Conta não encontrada.", "!")
    return conta


def main():
    LIMITE_SAQUES = 3
    AGENCIA_PADRAO = "0001"

    numero_saques = 0
    clientes = []
    contas = []

    while True:
        escolha = menu()

        if escolha == "d":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                depositar(conta, valor)

        elif escolha == "s":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                numero_saques = sacar(conta, valor, 500, numero_saques, LIMITE_SAQUES)

        elif escolha == "e":
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)

        elif escolha == "a":
            cadastrar_cliente(clientes)

        elif escolha == "c":
            numero_conta = len(contas) + 1
            conta = criar_nova_conta(AGENCIA_PADRAO, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif escolha == "l":
            exibir_contas(contas)

        elif escolha == "q":
            mostrar_msg("Encerrando o sistema. Até logo!", "#")
            break

        else:
            mostrar_msg("Opção inválida. Tente novamente.", "!")


main()