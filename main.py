import interpretador
import tabela


'''def criar_tabelas():
    t_employees = tabela.Tabela('tabelas/employees.csv', 'employees')
    t_employees.campos.append(tabela.Campo('emp_no', 'int'))
    t_employees.campos.append(tabela.Campo('birth_date', 'string'))
    t_employees.campos.append(tabela.Campo('first_name', 'string'))
    t_employees.campos.append(tabela.Campo('last_name', 'string'))
    t_employees.campos.append(tabela.Campo('gender', 'string'))
    t_employees.campos.append(tabela.Campo('hire_date', 'string'))

    base_de_dados.tabelas.append(t_employees)'''


# quando essa variavel eh passada como parametro, a funcao pode alterar o valor dessa lista.
executando = [True]

comando = ''
base_de_dados = tabela.BaseDeDados()

while executando[0]:
    print('->')
    comando = input()
    interpretador.interpreta_comando(comando, base_de_dados, executando)
