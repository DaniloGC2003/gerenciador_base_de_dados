import interpretador
import tabela


# quando essa variavel eh passada como parametro, a funcao pode alterar o valor dessa lista.
executando = [True]

comando = ''
base_de_dados = tabela.BaseDeDados()
base_de_dados.inicializar_tabelas()

while executando[0]:
    print('->', end=' ')
    comando = input()
    interpretador.interpreta_comando(comando, base_de_dados, executando)
