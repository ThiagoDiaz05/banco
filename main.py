from banco import Banco
banco = Banco()
while True:
    print("======BANCO======")
    print("1 - saldo")
    print("2 - deposito")
    print("3 - saque")
    print("digite qualquer outro numero pra sair")
    print("=================")
    try:
        numero = int(input(print("digite um numero: ")))
    except ValueError:
        print("escreva um numero valido")
        continue  
    match numero:
        case 1: banco.Saldo()
        case 2: banco.Deposito()
        case 3: banco.Saque()
        case _: break