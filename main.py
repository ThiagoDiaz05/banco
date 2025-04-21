from cliente import Cliente
from banco import Banco
from dinheiro import Dinheiro

banco = Banco()
cliente = Cliente()
d = Dinheiro(nome = "", saldo = 0)

while True:
    print("======BANCO======")
    nome_input = input("Digite seu nome: ")
    print("=================")
    
    cliente.confirir_conta(nome_input, banco, d,cliente)
