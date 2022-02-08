import operator
import os


def ordena(nome, iniciativa):
    dici = {}
    for i in range(len(nome)):
        dici.update({nome[i]: iniciativa[i]})

    dicionario_ordenado = dict(sorted(dici.items(),
                               key=operator.itemgetter(1), reverse=True))

    return dicionario_ordenado


def imprimi_na_tela(dicionario, contador):
    count = 0
    turno = 0
    rodada = 0
    condicao = True
    while condicao is True:
        print('RODADA {}'.format(rodada))

        for item in dicionario.items():
            if turno == len(dicionario.values()):
                turno = 0
                rodada += 1
            # elif turno == (len(dicionario.values())):
            contador[turno] = '>'
            print(contador[count], item[1], '-', item[0])
            contador[turno] = '_'
            count += 1
        count = 0
        turno += 1

        print('')
        proximo = input('Proximo Turno: (1) Sim | (2) Não: ')
        os.system('clear')

        if proximo == '1':
            pass
        else:
            condicao = False
