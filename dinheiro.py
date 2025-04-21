
class Dinheiro():
    def __init__(self,saldo, nome):
        self.saldo= saldo
        self.cliente = nome

    def getSaldo(self):
        return self.saldo   
    
    def getCliente(self):
        return self.cliente
        
    def setSaldo(self, novoSaldo):
        self.saldo = novoSaldo

    def setCliente(self, nome):
        self.cliente = nome
    