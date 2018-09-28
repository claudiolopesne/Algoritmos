# Importação da biblioteca
import sqlite3

# Função para criar a tabela
def criar_tabela_contato(conexao):

    # Cria o cursor para operar o BD
    cursor = conexao.cursor()

#Monta o sql
sql = """
    CREATE TABLE IF NOT EXISTS contato (
        nome text,
        fone text,
        email text,
        usuario integer
    );
"""

#Executa o SQL
cursor.execute (sql)

#Faz o commit para Salvar
conexao.commit()
