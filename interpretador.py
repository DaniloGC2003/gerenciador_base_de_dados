import tabela
import importacao_csv

palavras_do_comando = []  # lista em que cada elemento eh uma palavra


# preenche palavras_do_comando com as palavras que compoem a string digitada pelo usuario
def split_string(comando):
    palavras_do_comando.clear()
    palavra = ''
    for i in range(0, len(comando)):
        if comando[i] != ' ':
            if i == len(comando) - 1:  # ultimo char da string
                palavra += comando[i]
                palavras_do_comando.append(palavra)
                palavra = ''
            else:  # nao eh ultimo char da string
                palavra += comando[i]
        elif comando[i] == ' ':  # barra de espaco
            palavras_do_comando.append(palavra)
            palavra = ''


def importar_dados():
    pass


def interpreta_comando(comando, db, executando):

    erro = 0
    split_string(comando)
    print(palavras_do_comando)

    if comando == '':
        pass  # nao faz nada


    elif palavras_do_comando[0] == 'importação':
        if palavras_do_comando[1] == 'externa':  # base de dados externa
            pass
        elif palavras_do_comando[1] == 'local':  # arquivo csv local
            importacao_csv.importar_de_csv(db)
        else:
            erro = 1


    elif palavras_do_comando[0] == 'criar':
        if palavras_do_comando[1] == 'tabela':  # Cria uma nova tabela e o arquivo correspondente.
            campos = []
            i = 4
            if palavras_do_comando[3] == ':' \
                    or palavras_do_comando[2][len(palavras_do_comando[2])-1] == ':':
                if palavras_do_comando[2][len(palavras_do_comando[2])-1] == ':':
                    palavras_do_comando[2] = palavras_do_comando[2][:-1]
                    i = 3
                while palavras_do_comando[i][len(palavras_do_comando[i])-1] != '.':  # Sintaxe flexível.
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
            # criar tabela Teste: cam,po1, cam.po2.
            # Se a nova tabela tiver o mesmo nome que outra já existente,
            # a nova tabela não será criada
            # e o programa esperará a próxima instrução.

    elif palavras_do_comando[0] == 'sair':
        executando[0] = False

    else:
        erro = 1

    if erro != 0:
        print("ERRO: Expressão não reconhecida na posição {}.".format(erro))


def conectar_a_base_externa():
    host = input()
    usuario = input()
    senha = input()
    banco = input()
