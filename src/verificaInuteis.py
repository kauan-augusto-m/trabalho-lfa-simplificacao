def calculaGeradores(Gramatica):

    Geradores = []
    GeradoresTemp = []

    

    for cabeca, corpo in Gramatica.items():

        for elemento in corpo:

            cont = 0

            for letra in elemento:

                # terminal
                if letra not in Gramatica:
                    cont += 1

            if cont == len(elemento):

                if cabeca not in Geradores:
                    Geradores.append(cabeca)

    tam = len(Geradores)

    

    while True:

        for cabeca, corpo in Gramatica.items():

            for elemento in corpo:

                cont = 0

                for letra in elemento:

                    if letra not in Gramatica:
                        cont += 1

                    elif letra in Geradores:
                        cont += 1

                if cont == len(elemento):

                    if cabeca not in Geradores and cabeca not in GeradoresTemp:

                        GeradoresTemp.append(cabeca)

        Geradores.extend(GeradoresTemp)

        if len(Geradores) == tam:
            break

        else:
            tam = len(Geradores)
            GeradoresTemp.clear()

    return Geradores