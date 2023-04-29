import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host = "dbaula.ce1nbzgrn5ab.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "aulanoitefaculdade",
        database = "aula"
        )
        
    return mydb
    