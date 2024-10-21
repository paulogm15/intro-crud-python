import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'facsenac',
)

cursor = conexao.cursor()

comando = f'select * from usuarios;'

cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
conexao.close()
