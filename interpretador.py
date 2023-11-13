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

    split_string(comando)
    print(palavras_do_comando)

    if comando == '':
        pass  # nao faz nada
    elif palavras_do_comando[0] == 'importação':
        if palavras_do_comando[1] == 'externa':  # base de dados externa
            pass
        elif palavras_do_comando[1] == 'local':  # arquivo csv local
            importacao_csv.importar_de_csv(db)
    elif palavras_do_comando[0] == 'sair':
        executando[0] = False


def conectar_a_base_externa():
    host = input()
    usuario = input()
    senha = input()
    banco = input()
