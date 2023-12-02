import tabela
import importacao_csv
import conexao_externa
import misc
import joins
import where
import update

palavras_do_comando = []  # lista em que cada elemento eh uma palavra
limite_linhas = 100  # limite de linhas a serem impressas

# preenche palavras_do_comando com as palavras que compoem a string digitada pelo usuario


def split_string(comando):
    dentro_aspas = False
    palavras_do_comando.clear()
    palavra = ''
    for i in range(0, len(comando)):
        if not dentro_aspas:
            if comando[i] != ' ' and (comando[i] != '\'' and comando[i] != '\"'):
                if i == len(comando) - 1:  # ultimo char da string
                    palavra += comando[i]
                    palavras_do_comando.append(palavra)
                    palavra = ''
                else:  # nao eh ultimo char da string
                    palavra += comando[i]
            # barra de espaco
            elif comando[i] == ' ' and (comando[i-1] != '\'' and comando[i-1] != '\"'):
                palavras_do_comando.append(palavra)
                palavra = ''

            elif comando[i] == '\'' or comando[i] == '\"':
                dentro_aspas = True

            ''' print('aq' + comando[i])
                i += 1
                palavra = ''
                while (comando[i] != '\'' and comando[i] != '\"'):
                    print(comando[i])
                    palavra += comando[i]
                    i += 1
                palavras_do_comando.append(palavra)
                print(palavra)
                palavra = ''
                i += 2
                print('comando: ' + comando[i])'''
        else:
            if comando[i] != '\'' and comando[i] != '\"':
                palavra += comando[i]
            elif comando[i] == '\'' or comando[i] == '\"':
                dentro_aspas = False
                palavras_do_comando.append(palavra)
                palavra = ''


def interpreta_comando(comando, db, executando):
    i = 0
    erro = 0
    split_string(comando)
    # print(palavras_do_comando)
    # db.print_tabela()

    if comando == '':
        pass  # nao faz nada

    elif palavras_do_comando[0] == 'refresh':
        db.refresh()

    elif palavras_do_comando[0] == 'importação':
        if palavras_do_comando[1] == 'externa':  # base de dados externa
            conexao_externa.importar(db)
        elif palavras_do_comando[1] == 'local':  # arquivo csv local
            importacao_csv.importar_de_csv(db)
        else:
            erro = 1

    elif palavras_do_comando[0] == 'criar':
        # Cria uma nova tabela e o arquivo correspondente.
        if palavras_do_comando[1] == 'tabela':
            campos = []  # lista de strings
            i = 4
            if palavras_do_comando[3] == ':' \
                    or palavras_do_comando[2][len(palavras_do_comando[2])-1] == ':':
                if palavras_do_comando[2][len(palavras_do_comando[2])-1] == ':':
                    palavras_do_comando[2] = palavras_do_comando[2][:-1]
                    i = 3
                # Sintaxe flexível.
                while palavras_do_comando[i][len(palavras_do_comando[i])-1] != '.':
                    if palavras_do_comando[i][len(palavras_do_comando[i])-1] == ',':
                        campos.append(palavras_do_comando[i][:-1])
                    else:
                        campos.append(palavras_do_comando[i])
                    i = i + 1
                    if (i >= len(palavras_do_comando)):
                        break
                if (i < len(palavras_do_comando)):
                    campos.append(palavras_do_comando[i][:-1])
            else:
                erro = 4

            db.criar_tabela(campos, palavras_do_comando[2])
        else:
            erro = 2
            # Exemplos de sintaxe válida:
            # criar tabela Teste: campo1, campo2.
            # criar tabela Teste : campo1 campo2.
            # criar tabela Teste: cam,po1, cam.po2
            # Se a nova tabela tiver o mesmo nome que outra já existente,
            # a nova tabela não será criada
            # e o programa esperará a próxima instrução.

    elif palavras_do_comando[0] == 'inserir':
        if palavras_do_comando[1] == 'em':
            i = 4
            if palavras_do_comando[3] == ':' \
                    or palavras_do_comando[2][len(palavras_do_comando[2])-1] == ':':
                if palavras_do_comando[2][len(palavras_do_comando[2])-1] == ':':
                    palavras_do_comando[2] = palavras_do_comando[2][:-1]
                    i = 3
                arq_tabela = open(
                    "tabelas/" + palavras_do_comando[2] + ".csv", 'a+')
                pos = arq_tabela.tell()
                arq_tabela.seek(0)
                campos = arq_tabela.readline()   # Primeira linha com os campos

                if campos == '':
                    print("ERRO: Esta tabela está vazia.")
                    return 1
                campos = campos.split(sep=",")
                print((campos))
                x = 0
                while x < len(campos):
                    if campos[x][len(campos[x]) - 1] == ',' or campos[x][len(campos[x]) - 1] == '\n':
                        campos[x] = campos[x][:-1]
                    x = x + 1
                print(len(campos))
                if len(palavras_do_comando) - i != len(campos):
                    print(
                        "ERRO: Número de argumentos não corresponde ao número de campos.")
                    return 1
                arq_tabela.seek(pos)
                while i < len(palavras_do_comando):
                    if palavras_do_comando[i][len(palavras_do_comando[i]) - 1] == ',':
                        palavras_do_comando[i] = palavras_do_comando[i][:-1]
                    arq_tabela.write(palavras_do_comando[i])
                    if palavras_do_comando[i] != palavras_do_comando[len(palavras_do_comando)-1]:
                        arq_tabela.write(',')
                    else:
                        arq_tabela.write('\n')
                    i = i + 1
            else:
                erro = 4
        else:
            erro = 2

    # atualizar TABELA mudar CAMPO = VALOR onde EXPRESSÃO LÓGICA
    elif palavras_do_comando[0] == 'atualizar':
        novo_valor = []
        i = 5  # comeca no inicio da expressao que indica novo valor
        while palavras_do_comando[i] != 'onde':
            novo_valor.append(palavras_do_comando[i])
            i += 1

        i += 1
        palavra1 = palavras_do_comando[i]
        operador = palavras_do_comando[i+1]
        palavra2 = palavras_do_comando[i+2]
        update.atualizar_campos(palavras_do_comando[1], palavras_do_comando[3], novo_valor,
                                palavra1, operador, palavra2)

    elif palavras_do_comando[0] == 'deletar':
        if palavras_do_comando[1] == 'de':
            arq_tabela = open(
                "tabelas/" + palavras_do_comando[2] + ".csv", "r+")
            for tabela in db.tabelas:
                if tabela.nome == palavras_do_comando[2]:
                    tabelaSel = tabela
                    print("DELETE: Tabela = {}".format(palavras_do_comando[2]))
                    break

            if (palavras_do_comando[3] == 'onde'):
                if 7 < len(palavras_do_comando):
                    if palavras_do_comando[7] == 'ou' or palavras_do_comando[7] == 'e':
                        arq_tabela_filtrada, tabelaSel_filtrada = where.filtragem_2_campos(palavras_do_comando[2], db, palavras_do_comando[4], palavras_do_comando[5],
                                                                                           palavras_do_comando[6], palavras_do_comando[7], palavras_do_comando[8], palavras_do_comando[9], palavras_do_comando[10])
                        # i = i + 8
                        print("DELETE: WHERE chamado 1")
                    else:
                        arq_tabela_filtrada, tabelaSel_filtrada = where.filtragem_1_campo(
                            palavras_do_comando[2], db, palavras_do_comando[4], palavras_do_comando[5], palavras_do_comando[6])
                        # i = i + 4
                        print("DELETE: WHERE chamado 2")
                else:
                    arq_tabela_filtrada, tabelaSel_filtrada = where.filtragem_1_campo(
                        palavras_do_comando[2], db, palavras_do_comando[4], palavras_do_comando[5], palavras_do_comando[6])
                    print("DELETE: WHERE chamado 3")

            temp = arq_tabela
            print(tabelaSel_filtrada.registros)
            registros_deletados = []
            for reg in tabelaSel_filtrada.registros:
                if reg in tabelaSel.registros:
                    print("\n\n\n\n\n\n\nRegistro encontrado.\n\n\n\n\n\n")
                    registros_deletados.append(reg)
                    # stringreg = ""
                    # for camporeg in reg:
                    #    stringreg = stringreg + camporeg + ','
                    # stringreg = stringreg[:-1]
                    # stringreg = stringreg + '\n'
                    # registros_deletados.append(stringreg)

            arq_tabela.seek(0)
            campos = arq_tabela.readline()
            arq_tabela.close()
            print("arq_tabela fechado.")
            arq_tabela = open(
                "tabelas/" + palavras_do_comando[2] + ".csv", "w")
            arq_tabela.write(campos)
            for reg in tabelaSel.registros:
                if reg not in registros_deletados:
                    i = 1
                    for camporeg in reg:
                        arq_tabela.write(camporeg)
                        if i < len(reg):
                            arq_tabela.write(',')
                        else:
                            arq_tabela.write('\n')
                        i = i + 1
            # arq_tabela.write(temp)

    elif palavras_do_comando[0] == 'selecionar':
        i = 1
        camposSel = []
        camposNum = []
        if (palavras_do_comando[1] == '*'):
            arq_tabela = open(
                "tabelas/" + palavras_do_comando[3] + ".csv", 'r')
            temp = arq_tabela.readline()  # pega linha com nome dos campos
            temp = temp[:-1]  # elimina o \n do final
            camposSel = temp.split(sep=',')
            arq_tabela.close()
            i = 2
        else:
            while (palavras_do_comando[i] != 'de'):  # campos do 'selecionar'
                if palavras_do_comando[i][len(palavras_do_comando[i])-1] == ',':
                    palavras_do_comando[i] = palavras_do_comando[i][:-1]
                camposSel.append(palavras_do_comando[i])
                i = i + 1

        # print("camposSel: {}".format(camposSel))
        i = i + 1
        arq_tabela = open("tabelas/" + palavras_do_comando[i] + ".csv", 'r')
        camposTab = arq_tabela.readline()  # pega linha com nomes dos campos
        camposTab = camposTab[:-1]  # elimina o \n do final
        camposTab = camposTab.split(sep=',')  # todos os campos da tabela
        tabelaSel = None
        for iter in db.tabelas:
            if iter.nome == palavras_do_comando[i]:
                tabelaSel = iter  # objeto tabela
        # print("camposTab: {}".format(camposTab))

        # se ainda houver mais comandos
        if i + 1 < len(palavras_do_comando):  # msg esperada: juntar com TAB1 usando TAB2
            if palavras_do_comando[i+1] == 'onde':
                # arq_tabela.close()
                if i + 5 < len(palavras_do_comando):
                    if palavras_do_comando[i+5] == 'ou' or palavras_do_comando[i+5] == 'e':
                        arq_tabela, tabelaSel = where.filtragem_2_campos(palavras_do_comando[i], db, palavras_do_comando[i+2], palavras_do_comando[i+3],
                                                                         palavras_do_comando[i+4], palavras_do_comando[i+5], palavras_do_comando[i+6], palavras_do_comando[i+7], palavras_do_comando[i+8])
                        i = i + 8
                    else:
                        arq_tabela, tabelaSel = where.filtragem_1_campo(
                            palavras_do_comando[i], db, palavras_do_comando[i+2], palavras_do_comando[i+3], palavras_do_comando[i+4])
                        i = i + 4
                else:
                    arq_tabela, tabelaSel = where.filtragem_1_campo(
                        palavras_do_comando[i], db, palavras_do_comando[i+2], palavras_do_comando[i+3], palavras_do_comando[i+4])
                    i = i + 4
            if i+1 < len(palavras_do_comando):
                if palavras_do_comando[i+1] == 'juntar':
                    if palavras_do_comando[i+2] == 'com':
                        if palavras_do_comando[i+4] == 'usando':
                            arq_tabela.close()
                            arq_tabela, camposTab, tabelaSel = joins.join(
                                palavras_do_comando[i], palavras_do_comando[i+3], palavras_do_comando[i+5], db)
                            # camposSel = camposTab

                            # print('nova tabela depois do join:', end='')
                            # tabelaSel.printTabela()

                            i = i + 5  # fazer o join, incrementar i
                            # tal que i + 1 seja 'ordenar'
                            # (se estiver no comando).

            if i+1 < len(palavras_do_comando):
                if palavras_do_comando[i+1] == 'ordenar':
                    if palavras_do_comando[i+2] == 'por':
                        i = i + 3
                        camposOrdenar = []
                        while (palavras_do_comando[i][len(palavras_do_comando[i])-1] == ','):
                            camposOrdenar.append(palavras_do_comando[i][:-1])
                            i = i + 1
                            if i >= len(palavras_do_comando):
                                break

                        if i < len(palavras_do_comando):
                            camposOrdenar.append(palavras_do_comando[i])

                        misc.ordenar(camposOrdenar, tabelaSel)

        for campo in camposSel:
            j = 0
            while j < len(camposTab):
                if campo == camposTab[j]:
                    camposNum.append(j)  # índices dos campos selecionados
                    # print(campo)
                j = j + 1

        resultado = []
        tmp = arq_tabela.readline()
        while (tmp != ''):
            if tmp == '\n':
                tmp = arq_tabela.readline()
                continue
            tmp = tmp[:-1]
            tmp = tmp.split(sep=',')
            x = 0
            tmp2 = ''
            # print("camposNum: {}".format(camposNum))

            # cria string com campos selecionados
            while x < len(tmp):
                if x in camposNum:
                    tmp2 = tmp2 + tmp[x] + ','

                x = x + 1
                if x >= len(tmp):
                    tmp2 = tmp2[:-1]

            tmp = arq_tabela.readline()
            if tmp == '':
                if len(tmp2) >= 1:
                    if tmp2[len(tmp2) - 1] == ',':
                        tmp2 = tmp2[:-1]

            # print('tmp2: ' + tmp2)
            resultado.append(tmp2)

        print('tabela final: ')
        for linha in resultado:
            if resultado.index(linha) < limite_linhas:
                print(linha)
            else:
                break

    elif palavras_do_comando[0] == 'sair':
        executando[0] = False

    else:
        erro = 1

    if erro != 0:
        print("ERRO: Expressão não reconhecida na posição {}.".format(erro))
