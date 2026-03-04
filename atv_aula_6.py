Saldo = 1000



while True:
    print("------------------------Bem vindo ao bank------------------------")
    print(" 1 - Verificar \n 2 - Depositar  \n 3 - Sacar \n 4 - Sair")
    Escolha = int(input())
    
    if Escolha == 1:
        print(f"Seu saldo é:{Saldo}")
        continue


    elif Escolha == 2:
        print("Informe quanto sera depositado")
        Depositar = float(input())
        Saldo = Saldo + Depositar
        print(f"Valor a atualizado para:{Saldo}")
        continue

    elif Escolha == 3:
        print("Informe valor de saque")
        Saque = float(input())
        Saldo = Saldo - Saque
        print(f"Valor a atualizado para:{Saldo}")
        continue

    elif Escolha == 4:
        break

    else:
        print("Selecione um opção valida")
        continue
