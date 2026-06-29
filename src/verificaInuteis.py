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

def calculaAlcancaveis(Gramatica):

    Alc = ["S"]

    AlcTemp = []

    tam = len(Alc)

    while True:

        for cabeca, corpo in Gramatica.items():

            if cabeca in Alc:

                for elemento in corpo:

                    for letra in elemento:

                        if letra in Gramatica:

                            if letra not in Alc:

                                if letra not in AlcTemp:

                                    AlcTemp.append(letra)

        Alc.extend(AlcTemp)

        if len(Alc) == tam:

            break

        else:

            tam = len(Alc)

            AlcTemp.clear()

    return Alc


def procuraInuteis(Gramatica):

    Geradores = calculaGeradores(Gramatica)

    Alcancaveis = calculaAlcancaveis(Gramatica)

    Inuteis = []

    for simbolo in Gramatica:

        if simbolo not in Geradores:

            Inuteis.append(simbolo)

        elif simbolo not in Alcancaveis:

            Inuteis.append(simbolo)

    print("\nGeradores:")

    print(Geradores)

    print("\nAlcançáveis:")

    print(Alcancaveis)

    print("\nSímbolos inúteis:")

    print(Inuteis)

    return Inuteis