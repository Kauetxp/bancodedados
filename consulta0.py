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

#solicitando o usuario
busca = input("Digite o nome do usuario: ")

#executando consulta com LIKE

sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%",busca,"%",)
cursor.execute(sql, val)

#obtendo os resultados
results = cursor.fetchall()

#iterando sobre os resultados
for result in results:
    print(result)
#fechar a conexão com o servidor
conn.close

