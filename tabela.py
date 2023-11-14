import csv


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

        self.tabelas.append(tabela)


class Campo:
    def __init__(self, nome):
        self.nome = nome


class Tabela:
    def __init__(self, nome, caminho):
        self.nome = nome
        self.campos = []
        self.caminho = caminho

    '''def abrir_csv(self, caminho):
        with open(caminho, 'r') as csv_file:
            reader = csv.reader(csv_file)'''
