import csv


class BaseDeDados:
    def __init__(self):
        self.tabelas = []


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
