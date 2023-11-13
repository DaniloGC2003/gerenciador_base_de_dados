import csv
import tabela
import os

# funcoes para importar tabela a partir de arquivo csv


def importar_de_csv(db):
    # path do arquivo a ser importado
    caminho = input('caminho do arquivo a ser importado: ')

    with open(caminho, 'r') as csv_file:
        print('passou aq')
        reader = csv.reader(csv_file)

        nome_tabela = os.path.basename(caminho)  # extrair nome do arquivo csv
        print(nome_tabela)
        nome_tabela_sem_ext = nome_tabela[:-4]  # remover extensao do nome
        linhas = list(reader)

        with open('tabelas/' + nome_tabela, 'w') as new_table:
            print('passou aq tb')

            csv_writer = csv.writer(new_table)

            for line in linhas:
                print('oh')
                csv_writer.writerow(line)

        nova_tabela = tabela.Tabela(
            nome_tabela_sem_ext, 'tabelas/' + nome_tabela)

        for campo in linhas[0]:
            nova_tabela.campos.append(tabela.Campo(campo))
        db.tabelas.append(nova_tabela)
        print('campos da tabela: ')
        for x in nova_tabela.campos:
            print(x.nome)
