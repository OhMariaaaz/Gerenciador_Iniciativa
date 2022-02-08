import ordena_iniciativa
import confirma_pergunta
import os

confirm = True
nomes = []
iniciativas = []
i = 0


os.system('clear')
print('\tGERENCIADOR DE INICIATIVA')
print('====================================================')


# Recebendo os nomes e as iniciativas de cada personagem.
# Para cada repetição, um novo personagem é adicionado.
while confirm is True:
    i = i + 1

    # Recebendo o nome e a iniciativa do personagem.
    print('  PERSONAGEM ', i, ':')
    nome = input('DIGITE O NOME DO PERSONAGEM: ')
    iniciativa = input('DIGITE A INICIATIVA DO PERSONAGEM: ')

    # Adicionando nome e iniciativa nas listas.
    nomes.append(nome.title())
    iniciativas.append(str(iniciativa).rjust(2, '0'))

    # Criando uma nova repetição caso o usuário deseje.
    print('====================================================')
    msg = 'PERSONAGEM ADICIONADO! DESEJA ADICIONAR MAIS ALGUM?'
    confirm = confirma_pergunta.confirma(msg)
    os.system('clear')

print('====================================================')
print('\tORDEM DE INICIATIVA')

ordena_iniciativa.ordena(nomes, iniciativas)
