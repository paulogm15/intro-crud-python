import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'facsenac',
)

cursor = conexao.cursor()

cod = 'null'
nome = input('Digite o nome: ')
cidade = input('Digite a cidade do usuario: ')
uf = input('Digite a Unidade Federativa: ')
data = 'now()'

comando = f"Insert into usuarios values({cod}, '{nome}', '{cidade}', '{uf}', {data});"

cursor.execute(comando)
conexao.commit() #edita o banco
conexao.close()
