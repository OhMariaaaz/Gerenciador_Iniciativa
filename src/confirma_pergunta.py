def confirma(msg):
    # Envia a mensagem.
    print(msg)

    # Recebe a resposta e padroniza ela(caixa alta).
    resposta = input('(1) Sim | (2) Não')

    # Verifica qual foi a resposta do usuário e retorna.
    if resposta == "1":
        confirm = True
    else:
        confirm = False
    return confirm
