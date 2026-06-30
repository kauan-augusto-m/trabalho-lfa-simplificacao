def printGramatica(gramatica):

    for cabeca, corpo in gramatica.items():

        print(f"{cabeca} {corpo}")


def procuraProdUnitarias(Gramatica):

    GramaticaTemp = {}

    for cabeca, corpo in Gramatica.items():

        for elemento in corpo:

            # A -> B

            if len(elemento) == 1 and elemento in Gramatica:

                if cabeca in GramaticaTemp:

                    GramaticaTemp[cabeca].append(elemento)

                else:

                    GramaticaTemp[cabeca] = [elemento]

    if len(GramaticaTemp) > 0:

        print("\nEssa gramática contém produções unitárias:")

        printGramatica(GramaticaTemp)

    else:

        print("\nGramática não contém produções unitárias e está pronta para a próxima fase")
