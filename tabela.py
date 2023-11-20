import csv
import os


class BaseDeDados:
    def __init__(self):
        self.tabelas = []
        self.caminhos = []

    def criar_tabela(self, Campos, nome):
        try:
            arq_tabela = open("tabelas/"+nome+".csv", 'x')
        except:
            print("ERRO: Esta tabela já existe.")
            return 1

        writer = csv.writer(arq_tabela)
        tabela = Tabela(nome, nome+".csv")

        for Campo in Campos:
            print(Campo)
            tabela.campos.append(Campo)
            arq_tabela.write(Campo)
            if Campo != Campos[len(Campos)-1]:
                arq_tabela.write(',')

        arq_tabela.write('\n')
        arq_tabela.close()
        self.caminhos.append("tabelas/"+nome+".csv")

        # self.tabelas.append(tabela)
        self.inicializar_tabelas()

    # cria objetos Tabela a partir de arquivos csv ja existentes na pasta tabelas
    def inicializar_tabelas(self):
        arquivos_csv = os.listdir('tabelas/')
        print(arquivos_csv)

        x = 0
        for arquivo in arquivos_csv:
            with open('tabelas/' + arquivo, 'r') as file:
                reader = csv.reader(file)

                nome_tabela_sem_ext = arquivo[:-4]  # remover extensao do nome
                for tabela in self.tabelas:
                    if tabela.nome == nome_tabela_sem_ext:
                        # print("Tabela {} já existe.".format(nome_tabela_sem_ext))
                        continue

                linhas = list(reader)
                nomes_campos = linhas[0]

                new_table = Tabela(nome_tabela_sem_ext, 'tabelas/' + arquivo)
                for campo in nomes_campos:
                    new_table.campos.append(Campo(campo))

                # reg = file.readlines()
                l2 = []
                y = 1
                i = 0
                while y < len(linhas):
                    if linhas[y] == '\n':
                        y = y + 1
                        continue

                    if linhas[y] == []:
                        y = y + 1
                        continue
                    else:
                        # print(linhas[y])
                        l2.append(linhas[y])
                        i = i + 1
                    y = y + 1
                new_table.registros = l2
                # print(new_table.registros)
                self.tabelas.append(new_table)
                x = x + 1

    def print_tabela(self):  # funcao para debugging
        for tabela in self.tabelas:
            print(tabela.nome + ': ', end='')
            for campo in tabela.campos:
                print(campo.nome + ' ', end='')
            print('\n')


class Campo:
    def __init__(self, nome):
        self.nome = nome


class Tabela:
    def __init__(self, nome, caminho):
        self.nome = nome
        self.campos = []
        self.caminho = caminho
        self.registros = []

    def registrar(self, str):
        self.registros.append(str)

    def printTabela(self):
        print(self.nome + ': ', end='')
        for reg in self.registros:
            print(reg, end='\n')
        print('\n')

    '''def abrir_csv(self, caminho):
        with open(caminho, 'r') as csv_file:
            reader = csv.reader(csv_file)'''
