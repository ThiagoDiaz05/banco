import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('usuarios.db')

# Criar um cursor
cursor = conn.cursor()

# Criar a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, saldo REAL)''')

# Inserir alguns dados de exemplo
cursor.execute("INSERT INTO usuarios (nome, saldo) VALUES (?, ?)", ("João", 1500))
cursor.execute("INSERT INTO usuarios (nome, saldo) VALUES (?, ?)", ("Maria", 2500))

# Confirmar as mudanças
conn.commit()

# Fechar a conexão
conn.close()

print("Banco de dados 'usuarios.db' criado e dados inseridos.")
