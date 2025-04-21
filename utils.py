
def TelaBanco(nome, saldo, banco, d,cliente):
    d.setSaldo(saldo)
    d.setCliente(nome)
    while True:
        print(f"======BANCO:{nome}======")
        print("1 - saldo")
        print("2 - deposito")
        print("3 - saque")
        print("digite qualquer outro numero pra sair")
        print("=========================")
        try:
            numero = int(input("digite um numero: "))
        except ValueError:
            print("escreva um numero valido")
            return
        match numero:
            case 1: banco.Saldo(d)
            case 2: banco.Deposito(d,cliente)
            case 3: banco.Saque(d,cliente)
            case _: return
