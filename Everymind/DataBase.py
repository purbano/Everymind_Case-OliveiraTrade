#Importação de biblioteca
import sqlite3

#Estabelecendo a conexão com o banco de dados
conn = sqlite3.connect("UsuariosData.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    DataNascimento TEXT NOT NULL,
    Cpf TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""") #Executando um comando no SQL

print("Conectado ao Banco de Dados!")