import operator
import os


# Arrumando a ordem da iniciativa do maior para o menor.
def ordena(nome, iniciativa):
    dici = {}

    # Para cada valor na lista nome, uma chave e um valor no dicionario
    # é adicionado.
    for i in range(len(nome)):
        dici.update({nome[i]: iniciativa[i]})

    # Ordenando os valores do dicionário, em outro dicionário, do maior para o
    # menor.
    dicionario_ordenado = dict(sorted(dici.items(),
                               key=operator.itemgetter(1), reverse=True))

    # Retorna o dicionário ordenado.
    return dicionario_ordenado


# Contador de rodadas do combate.
def imprimi_na_tela(dicionario, contador):
    count = 0
    turno = 0
    rodada = 1
    condicao = True

    # O loop a seguir mantém o gerenciador de iniciativa ativo até o usuário
    # desejar cancelar
    while condicao is True:

        # A mensagem a seguir imprimi a rodada atual
        # que é incrimentada sempre que uma rodada é concluída
        if turno == len(dicionario.values()):
            rodada += 1
        print('RODADA {}'.format(rodada))

        # O loop a seguir imprimi na tela o nome e o valor de iniciativa
        # de todos os personagens adicionados ao combate, além disso,
        # coloca uma marcação '>' que funciona como um indicador de quem
        # é a vez de jogar caso a rodada seja concluída, o indicador retorna
        # para o começo da iniciativa.
        for item in dicionario.items():

            # A variavel 'turno' é usada para indicar onde o marcador deve ser
            # inserido ela começa no indice 0 da lista contador, e quando chega
            # ao final da lista reseta para o zero
            if turno == len(dicionario.values()):
                turno = 0

            # A lista recebe a marcação para servir de indicador, após isso
            # imprimi na tela o indicador, o nome e o valor de iniciativa da
            # pessoa. Além disso, é também impresso na tela todos os outros
            # personagens da iniciativa, e caso não seja a vez dele de jogar
            # é impresso o indicador '_'
            contador[turno] = '>'
            print(contador[count], item[1], '-', item[0])
            contador[turno] = '_'

            # O count é usado para imprimir todos os valores da lista
            # 'contador' de maneira incremental. Lembrando que: caso
            # seja o turno do personagem de jogar, será exibido o
            # indicador '>'
            count += 1

        # Após impresso as informações referentes ao primeiro turno
        # do combate, a variável count é resetada, e a variável turno
        # é incrimentada
        count = 0
        turno += 1

        # Cada vez que o usuário digiar 1 (Sim), o Loop irá imprimir
        # novamente indicador de turno, nome e iniciativa, quando
        # o loop percorrer por todos os personagens, uma rodada
        # é concluída
        print('')
        msg = 'Proximo Turno:'
        condicao = confirma(msg)
        os.system('clear')


# Função de confirmação de mensagem.
def confirma(msg):
    resposta = "0"

    # Envia a mensagem.
    print(msg)
    while resposta != "1" and resposta != "2":

        # Recebe a resposta e padroniza ela(caixa alta).
        resposta = input('(1) Sim | (2) Não: ')

        # Verifica qual foi a resposta do usuário e retorna o resultado.
        # Caso a resposta não seja nem 1 e nem 2, o usuário deve digitar a
        # resposta novamente.
        if resposta == "1":
            confirm = True
        elif resposta == "2":
            confirm = False
        else:
            print("Resposta inválida! Digite novamente a sua resposta: ")

    return confirm
