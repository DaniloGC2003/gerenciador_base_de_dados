import csv
import tabela
import os

# funcoes para importar tabela a partir de arquivo csv


def importar_de_csv(db):
    # path do arquivo a ser importado
    caminho = input('caminho do arquivo a ser importado: ')

    with open(caminho, 'r') as csv_file:
        reader = csv.reader(csv_file)

        nome_tabela = os.path.basename(caminho)  # extrair nome do arquivo csv
        nome_tabela_sem_ext = nome_tabela[:-4]  # remover extensao do nome
        linhas = list(reader)

        with open('tabelas/' + nome_tabela, 'w') as new_table:

            csv_writer = csv.writer(new_table)

            for line in linhas:
                csv_writer.writerow(line)

        nova_tabela = tabela.Tabela(
            nome_tabela_sem_ext, 'tabelas/' + nome_tabela)

        for campo in linhas[0]:
            nova_tabela.campos.append(campo)
        db.tabelas.append(nova_tabela)
