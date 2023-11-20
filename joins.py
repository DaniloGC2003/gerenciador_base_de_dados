import tabela
import csv

# faz o inner join de tabela1 com tabela2 de acordo com campo.


def join(tabela1, tabela2, campo):
    # print(tabela1, tabela2)

    arq_tabela1 = open(
        "tabelas/" + tabela1 + ".csv", 'r')
    temp = arq_tabela1.readline()  # string com nomes dos campos
    temp = temp[:-1]  # elimina o \n do final
    campos1 = temp.split(sep=',')  # lista com nomes dos campos
    arq_tabela1.close()

    arq_tabela2 = open(
        "tabelas/" + tabela2 + ".csv", 'r')
    temp = arq_tabela2.readline()  # string com nomes dos campos
    temp = temp[:-1]  # elimina o \n do final
    campos2 = temp.split(sep=',')  # lista com nomes dos campos
    arq_tabela2.close()

    # posicao do campo a ser utilizado no join
    pos_tabela1 = campos1.index(campo)
    pos_tabela2 = campos2.index(campo)
    # print(pos_tabela1)
    # print(pos_tabela2)

    '''print(campos1)
    print(campos2)'''

    tuplas = []  # lista de tuplas
    with open("tabelas/" + tabela1 + ".csv", 'r') as csv_file1:
        reader1 = csv.reader(csv_file1)
        linhas1 = list(reader1)
        # print('linhas 1:')
        # print(linhas1)
        with open("tabelas/" + tabela2 + ".csv", 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            linhas2 = list(reader2)
            # print('linhas 2: ')
            # print(linhas2)
            for linha1 in linhas1:
                if len(linha1) != 0 and linha1 != linhas1[0]:
                    # print(linha1)
                    for linha2 in linhas2:
                        if len(linha2) != 0 and linha2 != linhas2[0]:
                            if linha1[pos_tabela1] == linha2[pos_tabela2]:
                                tuplas.append(linha1 + linha2)

    with open('tabelas_temporarias/' + 'join_' + tabela1 + '_' + tabela2 + '.csv', 'w') as new_table:
        csv_writer = csv.writer(new_table)

        csv_writer.writerow(campos1 + campos2)

        for tupla in tuplas:
            csv_writer.writerow(tupla)


# join('student', 'takes', 'ID')
