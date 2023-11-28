import tabela
import csv

def criar_objeto_tabela_temp(nomeTabela, db):
    novaTabela = tabela.Tabela(
        nomeTabela, 'tabelas_temporarias/' + nomeTabela + '.csv')
    db.tabelas.append(novaTabela)

    return novaTabela

def filtragem_1_campo(tabela, db, palavra1, operador, palavra2):#retorna 
    tabela_nova = criar_objeto_tabela_temp(tabela + '_filtrada', db)
    
    arq_tabela = open(
        "tabelas/" + tabela + ".csv", 'r')
    arq_tabela_reader = csv.reader(arq_tabela)
    linhas = list(arq_tabela_reader)#lista com todas as linhas do arquivo csv

    temp = arq_tabela.readline()  # string com nomes dos campos
    temp = temp[:-1]  # elimina o \n do final
    campos = temp.split(sep=',')  # lista com nomes dos campos da tabela dada
    #arq_tabela1.close()

    tabela_nova.campos = campos

    if operador == '=':
        arq_tabelaTemp = open("tabelas_temporarias/" + tabela_nova.nome + ".csv", 'w')
        