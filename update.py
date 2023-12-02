import csv
import where


def calcula_expressao(operacao, valor1, valor2):
    if operacao == '+':
        return float(valor1) + float(valor2)
    elif operacao == '*':
        return float(valor1) * float(valor2)
    elif operacao == '-':
        return float(valor1) - float(valor2)
    elif operacao == '/':
        return float(valor1) / float(valor2)


def retorna_novo_valor(tupla, posicao, novo_valor):
    valor = ''
    if len(novo_valor) == 1:
        if novo_valor[0].isnumeric():
            valor = float(novo_valor[0])
        else:
            valor = novo_valor[0]
    else:  # se for algo como campo * 2
        valor_antigo = float(tupla[posicao])
        valor = calcula_expressao(novo_valor[1], valor_antigo, novo_valor[2])

    return str(valor)


def atualizar_campos(tabela, campo, novo_valor, palavra1, operador, palavra2):
    linhas = []
    with open('tabelas/' + tabela + '.csv', 'r') as tabela_csv:
        reader = csv.reader(tabela_csv)
        linhas = list(reader)

    posicao_campo = linhas[0].index(campo)
    posicao_palavra1 = linhas[0].index(palavra1)

    for linha in linhas:  # atualizar valores
        if len(linha) != 0 and linha != linhas[0]:
            if where.avaliar_expressao(linha, posicao_palavra1, operador, palavra2):
                linha[posicao_campo] = retorna_novo_valor(
                    linha, posicao_campo, novo_valor)

    with open('tabelas/' + tabela + '.csv', mode='w', newline='') as tabela_csv_write:
        csv_writer = csv.writer(tabela_csv_write)
        csv_writer.writerows(linhas)

    print('Valores atualizados')
