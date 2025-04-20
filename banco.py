from dinheiro import Dinheiro

d = Dinheiro()

class Banco:
    def Saldo(self):
        print("======Saldo======")
        print(d.getSaldo())  
        print("=================")

    def Deposito(self):
        print("=====Depósito=====")
        try:
            deposito = float(input("Digite quanto você quer depositar: "))
        except ValueError:
            print("Por favor, insira um valor válido.")
            return
        if deposito > 0:
            saldo = d.getSaldo() + deposito  
            d.setSaldo(saldo)
            self.Saldo()  
        else:
            print("O valor precisa ser maior que 0.")

    def Saque(self):
        print("=====Saque=====")
        try:
            saque = float(input("Digite quanto você quer sacar: "))
        except ValueError:
            print("Por favor, insira um valor válido.")
            return
        if saque > 0:
            if d.getSaldo() >= saque:
                saldo = d.getSaldo() - saque
                d.setSaldo(saldo)
                self.Saldo()  
            else:
                print("Você não pode sacar um valor maior do que seu saldo.")
        else:
            print("O valor precisa ser maior que 0.")

