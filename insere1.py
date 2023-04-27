import mysql.connector

#Criando um dicionario de informações
config = {
    "user": "admin",
    "password": "aulanoitefaculdade",
    "host": "dbaula.ce1nbzgrn5ab.us-east-1.rds.amazonaws.com",
    "database": "aula"
}

# Estabelecendo conexão com o banco
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()


# Pedindo ao usuario

nome_estado = input("Digite o nome do estado: ")
codigo_estado = int(input("Digite o código do estado: "))

# Inserindo o estado na tabela
sql = "INSERT INTO estado (codigo, nome) VALUES (%s, %s)"
val = (codigo_estado, nome_estado)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()