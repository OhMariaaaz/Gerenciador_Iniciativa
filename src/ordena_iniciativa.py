lista_de_nomes = ['Júlio', 'Eduarda', 'Luiz']
lista_de_numeros = [20, 20, 13]
cond_life = 'Vivo'
cond_life_2 = 'Morto'
condicao = True
dici = {}
lista = []

for i in range(3):
    dici.update({lista_de_nomes[i]: lista_de_numeros[i]})


print('ORDEM DA INICIATIVA')
for item in dici.items():
    print(item[1], '-', item[0])
