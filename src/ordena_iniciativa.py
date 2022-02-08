import operator


def ordena(nome, iniciativa):
    dici = {}
    for i in range(len(nome)):
        dici.update({nome[i]: iniciativa[i]})

    novo_dic = dict(sorted(dici.items(), key=operator.itemgetter(1),
                    reverse=True))

    for item in novo_dic.items():
        print(item[1], '-', item[0])
