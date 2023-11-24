import tabela
import math

def ordenar(campo, table):
    x = 0
    ind = []
    #print(table.campos)
    #print(table.campos[0].nome + "vs. " + campo)
    #for Campo in table.campos:
    #    print(Campo.nome)
    #    if campo == Campo.nome:
    #        ind = x
    #    x = x + 1

    campo.reverse()

    for CampoO in campo:
        for CampoT in table.campos:
            print("{}, {}".format(CampoO, CampoT.nome))
            if CampoO == CampoT.nome:
                ind.append(x)
            x = x + 1
        x = 0


    if ind == []:
        print("(ordenar) ERRO: Campo solicitado não faz parte da tabela")
        return 1

    print(ind)
    o = 0
    while o < len(ind):
        mergeSort(table,ind[o],0,len(table.registros)-1)
        o = o + 1

    table.printTabela()


def mergeSort(table,campo,imin,imax):
    if imin == imax:
        return

    
    mergeSort(table,campo,imin,imin+math.floor((imax-imin)/2))
    mergeSort(table,campo,1+imin+math.floor((imax-imin)/2),imax)

    print("{}, {}".format(imin, imax))
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

        elif x > imin+math.floor((imax-imin)/2) or regy[campo] < regx[campo]:
            #aux = table.registros[y]
            #table.registros[y] = table.registros[iter]
            #table.registros[iter] = aux
            res.append(table.registros[y])
            iter = iter + 1
            y = y + 1
            if y > imax:
                regy = None
                continue

            regy = table.registros[y]

        elif y > imax or regy[campo] >= regx[campo]:
            #aux = table.registros[x]
            #table.registros[x] = table.registros[iter]
            #table.registros[iter] = aux
            res.append(table.registros[x])
            iter = iter + 1
            x = x + 1
            if x > imin+math.floor((imax-imin)/2):
                regx = None
                continue

            regx = table.registros[x]
    
    for i in range(imin,imin+len(res)):
        table.registros[i] = res[i-imin]
