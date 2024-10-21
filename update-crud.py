import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'facsenac',
)

cursor = conexao.cursor()

cod = '2'
nome = 'Cesar Cielo'

comando = f'update usuarios set nome="{nome}" where cod={cod}'

cursor.execute(comando)
conexao.commit()
conexao.close()
