import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'facsenac',
)

cursor = conexao.cursor()

cod = 2;

comando = f'delete from usuarios where cod={cod}'

cursor.execute(comando)
conexao.commit()

print(f'Cod {cod} excluida com sucesso')
conexao.close()
