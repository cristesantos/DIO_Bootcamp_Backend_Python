# Sistema do Banco
# Req1: Conta única
# Req2: Permitir operação de saque, extrato e depósito
# Req3: Todos os depósitos devem ser armazenados em uma variável e exibidos pela operação extrato
# Req4: Permitir realizar 3 saques diários com limite de 500 por saque
# Req5: Se não houver saldo, deve exibir uma mensagem
# Req6: Todos os saques devem ser armazenados em uma variável e exibidos pela operação extrato
# Req7: A operação extrato deve exibir os depósitos, saques e o saldo atual
# Req8: Os valores exibidos devem ter formato R$ xxx.xx

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''
saldo = 0
limite_saque = 500
saques_realizados = 0
extrato = ""
limite_saque_diario = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    elif opcao == "s":
        if saques_realizados < limite_saque_diario:
            valor = float(input("Informe o valor do saque: "))
            if valor <= saldo and valor <= limite_saque:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                saques_realizados += 1
            else:
                print("Saque não permitido por falta de fundos.")
        else:
            print("Limite de saques diários atingido.")
    elif opcao == "e":
        print("=== Extrato ===")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida.")