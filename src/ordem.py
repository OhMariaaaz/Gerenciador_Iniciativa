import ordena_iniciativa
import os

confirm = True
nomes = []
iniciativas = []
os.system('clear')
print('====================================================')
print('Seja bem vindo ao gerenciador de iniciativa! Vamos começar:')
i = 1

# Recebendo os nomes e as iniciativas de cada personagem.
# Para cada repetição, um novo personagem é adicionado.
while confirm is True:
    # Recebendo o nome e a iniciativa do personagem.
    print('\tPersonagem ', i, ':')
    nome = input('Digite o nome do personagem: ')
    iniciativa = input('Digite a iniciativa do personagem: ')

    # Adicionando nome e iniciativa nas listas.
    nomes.append(nome.title())
    iniciativas.append(str(iniciativa).rjust(2, '0'))

    print('====================================================')

    # Criando uma nova repetição no While caso o usuário deseje.
    print('Personagem adicionado na lista!')
    resposta = input('Deseja adicionar mais algum? ')
    resposta = resposta.upper()
    if resposta == "SIM" or resposta == "S":
        confirm = True
    elif resposta == "YES" or resposta == "Y":
        confirm = True
    else:
        confirm = False
    i = i + 1
    os.system('clear')

print('====================================================')
print('Iniciativas inseridas. Vamos começar o combate!')

dicionario_ordenado = ordena_iniciativa.ordena(nomes, iniciativas)
contador = ['_' for item in dicionario_ordenado.items()]
ordena_iniciativa.imprimi_na_tela(dicionario_ordenado, contador)
