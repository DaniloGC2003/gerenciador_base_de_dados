# funcoes para se conectar a uma base de dados MySQL externa

import MySQLdb

# retorna conexao ao banco de dados escolhido
def conectar_mysql(host, usuario, senha, banco):
    conexao = MySQLdb.connect(host=host, user=usuario, passwd=senha, db=banco)
    return conexao


def criar_cursor(conexao):  # retorna cursor para execucao de comandos sql
    cursor = conexao.cursor()
    return cursor


def fechar_conexao(conexao, cursor):  # fecha conexao ao banco de dados
    cursor.close()
    conexao.close()
