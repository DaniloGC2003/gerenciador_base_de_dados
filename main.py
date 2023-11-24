import interpretador
import tabela
import os


# quando essa variavel eh passada como parametro, a funcao pode alterar o valor dessa lista.
executando = [True]

comando = ''
base_de_dados = tabela.BaseDeDados()
base_de_dados.inicializar_tabelas()

while executando[0]:
    print('->', end=' ')
    comando = input()
    interpretador.interpreta_comando(comando, base_de_dados, executando)

'''# apagar arquivos csv temporarios
arquivos_csv = os.listdir('tabelas_temporarias/')
print(arquivos_csv)
for arquivo in arquivos_csv:
    if os.path.exists('tabelas_temporarias/' + arquivo):
        os.remove('tabelas_temporarias/' + arquivo)'''
