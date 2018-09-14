# importa uma biblioteca para poder usar o seu conteudo
import  sqlite3
###############FUNÇÕES##########

def criar_tabela_usuario(cursor):


#monta o sql a  ser executado
    sql = """
        CREATE table IF NOT EXISTS usuario(
            nome text,
            login text,
            senha text
            );
        """
        #EXECULTA UM sql
        cursor.execute(sql)

def inserir_usuario(conexao):


    #cria o cursor para operar o banco
    cursor+conexao.cursor()



#################################
#iniciar uma conexão (ligação com nosso) banco
conexao = sqlite3.connect("aula28.sqlite")

#2 - Definir um meio de operar/exe
#Seria como se ele enviasse
cursor = conexao.cursor()

###########Criação de um banco de dados ###################



############### Inserindo um registro####################
nome = input ("nome:")
login = input ("login:")
senha = input ("senha:")

sql = """
    INSERT INTO usuario VALUES (
        '{}',
        '{}',
        '{}'
    );
""".format(nome, login, senha)
#Executa o sql
cursor.execute(sql)

#Salvar as modificações.
#O commit sempre deve ser feito apos a inserção no banco
conexao.commit()


























#Fechando a conexão
conexao.close()
