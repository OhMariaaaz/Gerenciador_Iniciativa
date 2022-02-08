def ordena(nome, iniciativa):
    dici = {}
    for i in range(len(nome)):
        dici.update({nome[i]: iniciativa[i]})

    for item in dici.items():
        print(item[1], '-', item[0])
