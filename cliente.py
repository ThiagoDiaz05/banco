import sqlite3
from utils import TelaBanco


class Cliente():
    def confirir_conta(self, nome, banco, d,cliente):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
        dados = cursor.fetchone()

        if dados:
            nome = dados[0]
            saldo = dados[1]
            TelaBanco(nome, saldo, banco, d,cliente)
        else:
            print("nao existe essa conta.")
            return 
    
    def depositar_saldo(self, saldo, nome_cliente):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE usuarios SET saldo = ? WHERE nome = ?", (saldo, nome_cliente))
    
        conn.commit()
        conn.close()

    def saque_saldo(self, saldo, nome_cliente):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE usuarios SET saldo = ? WHERE nome = ?", (saldo, nome_cliente))
    
        conn.commit()
        conn.close()
