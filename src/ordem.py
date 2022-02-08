import ordena_iniciativa

confirm = True
nomes = []
iniciativas = []
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
    nomes.append(nome)
    iniciativas.append(int(iniciativa))

    print('====================================================')

    # Criando uma nova repetição no While caso o usuário deseje.
    print('Personagem adicionado na lista!')
    resposta = input('Deseja adicionar mais algum?')
    resposta = resposta.upper()
    if resposta == "SIM" or resposta == "S":
        confirm = True
    elif resposta == "YES" or resposta == "Y":
        confirm = True
    else:
        confirm = False
    i = i + 1

print('====================================================')
print('Iniciativas inseridas. Vamos começar o combate!')

ordena_iniciativa.ordena(nomes, iniciativas)
