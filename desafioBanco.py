import time
import datetime

LIMITE_SAQUE = 3
saldo = 0
extrato = ""
numero_saque = 0
limite_saque = 500

print("BEM VINDO AO BANCO LIFE MONEY")
print("Carregando menu...")

time.sleep(2)

menu = """
================== MENU ====================

[1] Depositar
[2] Sacar
[3] Extrato
[4] Configurações (Em produção)
[0] Sair

============================================"""

erro = """=================================================
  ATENÇÃO: Digite uma opção válida de operação!
================================================="""

while True:
    print(menu)

    opcao = int(input("Selecione uma opção do menu:  "))

    # DEPOSITO
    if opcao == 1:
        print("\nServiços de DEPÓSITO")
        valor = int(input("Digite quanto deseja depositar: "))

        if valor <= 0:
            while valor <=0:
                print("Valor inválido!")
                valor = int(input("Digite uma valor válido para depositar: "))
        saldo += valor
        hora_atual = datetime.datetime.now()
        print(f"\nValor de R$ {valor:.2f} depositado na sua conta!")
        extrato += f"{hora_atual} --> Depósito: R$ {valor:.2f}\n"
        print(f"Seu novo saldo é: R$ {saldo:.2f}")

    # SAQUE
    elif opcao == 2:
        print("\nServiços de SAQUE")

        if numero_saque < LIMITE_SAQUE:
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
            valor = int(input("\nDigite um valor para realizar o saque: "))

            if valor <= 0:
                while valor <= 0:
                    print("Valor inválido!")
                    valor = int(input("Digite um valor válido para realizar o saque: "))

            elif valor > saldo:
                print("Saldo insuficiente!")

            else:
                while valor > limite_saque:
                    print("O limite por saque é R$", limite_saque)
                    valor = int(input("Digite um valor válido para realizar o saque: "))

                saldo -= valor
                numero_saque += 1
                hora_atual = datetime.datetime.now()
                print("Saque realizado com sucesso!")
                extrato += f"{hora_atual} --> Saque: R$ {valor:.2f}\n"
                print(f"Seu novo saldo é: R$ {saldo:.2f}")
        
        else:
            print("Limite de saques atingido!")
            print(f"Seu limite de saque é {LIMITE_SAQUE}, caso queira alterar vá em configurações [4] e solicite um novo limite.")

    # EXTRATO
    elif opcao == 3:
        print("\nOperação de EXTRATO\n")
        print(extrato)

        print(f"Seu saldo atual na conta é: R$ {saldo:.2f}")
    
    # SAIR
    elif opcao == 0:
        print("Saindo do sistema...")
        time.sleep(2)
        print("Obrigado por utilizar nossos serviços!")
        break

    # CONFIGURAÇÕES (EM ANDAMENTO)
    elif opcao == 4:
        print("Saindo do sistema...")
        time.sleep(2)
        print("Obrigado por utilizar nossos serviços!")
        break

    # ERRO DO MENU
    else:
        print(erro)