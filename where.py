import tabela
import csv


def criar_objeto_tabela_temp(nomeTabela, db):
    novaTabela = tabela.Tabela(
        nomeTabela, 'tabelas_temporarias/' + nomeTabela + '.csv')
    db.tabelas.append(novaTabela)

    return novaTabela


def filtragem_1_campo(tabela, db, palavra1, operador, palavra2):  # retorna
    # print(tabela + palavra1 + palavra2 + operador)
    tabela_nova = criar_objeto_tabela_temp(tabela + '_filtrada', db)

    arq_tabela = open(
        "tabelas/" + tabela + ".csv", 'r')
    arq_tabela_reader = csv.reader(arq_tabela)
    # lista com todas as linhas do arquivo csv
    linhas = list(arq_tabela_reader)
    # print(linhas)
    arq_tabela.close()

    campos = linhas[0]

    tabela_nova.campos = campos

    # posicao do campo utilizado na filtragem
    posicao_campo = campos.index(palavra1)

    arq_tabelaTemp = open("tabelas_temporarias/" +
                          tabela_nova.nome + ".csv", 'w')
    csv_writer = csv.writer(arq_tabelaTemp)

    if operador == '=':
        for linha in linhas:
            if linha != linhas[0] and len(linha) != 0:
                if linha[posicao_campo] == palavra2:
                    csv_writer.writerow(linha)
                    tabela_nova.registrar(linha)
    elif operador == '>=':
        for linha in linhas:
            if linha != linhas[0] and len(linha) != 0:
                if float(linha[posicao_campo]) >= float(palavra2):
                    csv_writer.writerow(linha)
                    tabela_nova.registrar(linha)
    elif operador == '>':
        for linha in linhas:
            if linha != linhas[0] and len(linha) != 0:
                if float(linha[posicao_campo]) > float(palavra2):
                    csv_writer.writerow(linha)
                    tabela_nova.registrar(linha)
    elif operador == '<=':
        for linha in linhas:
            if linha != linhas[0] and len(linha) != 0:
                if float(linha[posicao_campo]) <= float(palavra2):
                    csv_writer.writerow(linha)
                    tabela_nova.registrar(linha)
    elif operador == '<':
        for linha in linhas:
            if linha != linhas[0] and len(linha) != 0:
                if float(linha[posicao_campo]) < float(palavra2):
                    csv_writer.writerow(linha)
                    tabela_nova.registrar(linha)
    elif operador == '!=':
        for linha in linhas:
            if linha != linhas[0] and len(linha) != 0:
                if linha[posicao_campo] != palavra2:
                    csv_writer.writerow(linha)
                    tabela_nova.registrar(linha)

    arq_tabelaTemp.close()

    return open(tabela_nova.caminho, 'r'), tabela_nova
