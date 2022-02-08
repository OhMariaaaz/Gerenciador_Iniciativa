import operator
import os


# Arrumando a ordem da iniciativa do maior para o menor.
def ordena(nome, iniciativa):
    dici = {}

    # Para cada valor na lista nome, uma chave e um valor no dicionario
    # é adicionado.
    for i in range(len(nome)):
        dici.update({nome[i]: iniciativa[i]})

    # Ordenando os valores do dicionário, em outro dicionário, do maior para o menor.
    dicionario_ordenado = dict(sorted(dici.items(),
                               key=operator.itemgetter(1), reverse=True))

    # Retorna o dicionário ordenado.
    return dicionario_ordenado


'
ção A fun
'''
def imprimi_na_tela(dicionario, contador):
    count = 0
    turno = 0
    rodada = 1
    condicao = True
    while condicao is True:
        print('RODADA {}'.format(rodada))
        for item in dicionario.items():
            if turno == len(dicionario.values()):
                turno = 0
                rodada += 1
<<<<<<< HEAD

=======
>>>>>>> 52a8612a5ac87712dd2fe223b593f4294ce3e692
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


# Função de confirmação de mensagem.
def confirma(msg):
    resposta = "0"

    # Envia a mensagem.
    print(msg)
    while resposta != "1" and resposta != "2":

        # Recebe a resposta e padroniza ela(caixa alta).
        resposta = input('(1) Sim | (2) Não')

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
