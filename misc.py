import tabela
import math


def ordenar(campo, table):  # recebe campo (list) e table(objeto tabela)
    x = 0
    ind = []
    num = []
    # print(table.campos)
    # print(table.campos[0].nome + "vs. " + campo)
    # for Campo in table.campos:
    #    print(Campo.nome)
    #    if campo == Campo.nome:
    #        ind = x
    #    x = x + 1

    campo.reverse()

    for CampoO in campo:
        for CampoT in table.campos:
            # print("{}, {}".format(CampoO, CampoT.nome))
            if CampoO == CampoT:
                ind.append(x)
            if is_number(table.registros[0][x]) == 1:
                num.append(1)
            else:
                num.append(0)
            x = x + 1
        x = 0

    if ind == []:
        print("(ordenar) ERRO: Campo solicitado não faz parte da tabela")
        return 1

    #print(ind)
    #table.printTabela()
    #print(num)
    o = 0
    while o < len(ind):
        mergeSort(table, ind[o], 0, len(table.registros)-1, num[ind[o]])
        o = o + 1

    #table.printTabela()

    return table


def mergeSort(table, campo, imin, imax, num):
    if imin == imax:
        return

    mergeSort(table, campo, imin, imin+math.floor((imax-imin)/2), num)
    mergeSort(table, campo, 1+imin+math.floor((imax-imin)/2), imax, num)

    #print("{}, {}".format(imin, imax))
    x = imin
    y = 1 + imin+math.floor((imax-imin)/2)
    iter = imin
    regx = table.registros[x]
    regy = table.registros[y]
    res = []

    while x <= imin+math.floor((imax-imin)/2) or y <= imax:
        if regx == None:
            res.append(table.registros[y])
            iter = iter + 1
            y = y + 1
            if y >= imax:
                regy = None
                break

            regy = table.registros[y]

        elif regy == None:
            res.append(table.registros[x])
            iter = iter + 1
            x = x + 1
            if x > imin+math.floor((imax-imin)/2):
                regx = None
                break

            regx = table.registros[x]

        elif (x > imin+math.floor((imax-imin)/2) or regy[campo] < regx[campo]) and num == 0:
            # aux = table.registros[y]
            # table.registros[y] = table.registros[iter]
            # table.registros[iter] = aux
            res.append(table.registros[y])
            iter = iter + 1
            y = y + 1
            if y > imax:
                regy = None
                continue

            regy = table.registros[y]

        elif (y > imax or regy[campo] >= regx[campo]) and num == 0:
            # aux = table.registros[x]
            # table.registros[x] = table.registros[iter]
            # table.registros[iter] = aux
            res.append(table.registros[x])
            iter = iter + 1
            x = x + 1
            if x > imin+math.floor((imax-imin)/2):
                regx = None
                continue

            regx = table.registros[x]

        elif num == 1 and (x > imin+math.floor((imax-imin)/2) or float(regy[campo]) < float(regx[campo])):
            # aux = table.registros[y]
            # table.registros[y] = table.registros[iter]
            # table.registros[iter] = aux
            res.append(table.registros[y])
            iter = iter + 1
            y = y + 1
            if y > imax:
                regy = None
                continue

            regy = table.registros[y]

        elif num == 1 and (y > imax or float(regy[campo]) >= float(regx[campo])):
            # aux = table.registros[x]
            # table.registros[x] = table.registros[iter]
            # table.registros[iter] = aux
            res.append(table.registros[x])
            iter = iter + 1
            x = x + 1
            if x > imin + math.floor((imax - imin) / 2):
                regx = None
                continue

            regx = table.registros[x]

    for i in range(imin, imin+len(res)):
        table.registros[i] = res[i-imin]

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
