# funcoes para se conectar a uma base de dados MySQL externa

import MySQLdb
import csv
import tabela as tb

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


def input_informacoes():
    host = input('tipo de host: ')
    usuario = input('nome do usuário: ')
    senha = input('senha: ')
    banco = input('banco de dados a ser utilizado: ')
    tabela = input('nome da tabela a ser extraída: ')

    return (host, usuario, senha, banco, tabela)


def importar(db):
    host, usuario, senha, banco, tabela = input_informacoes()
    conexao = conectar_mysql(host, usuario, senha, banco)
    cursor = criar_cursor(conexao)
    cursor.execute('select * from ' + tabela)
    linhas = cursor.fetchall()

    with open('tabelas/' + tabela + '.csv', 'w') as new_table:
        csv_writer = csv.writer(new_table)

        # escrever nomes das colunas
        csv_writer.writerow([i[0] for i in cursor.description])

        # escrever linhas no arquivo
        for linha in linhas:
            csv_writer.writerow(linha)

    '''nova_tabela = tb.Tabela(tabela, 'tabelas/' + tabela)

    for campo in linhas[0]:
        nova_tabela.campos.append(campo)
    db.tabelas.append(nova_tabela)'''

    db.inicializar_tabelas()

    conexao.close()
