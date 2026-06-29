def calculaGeradores(Gramatica):
    Geradores = []
    GeradoresTemp = []

    # Caso base: produções compostas puramente por terminais
    for cabeca, corpo in Gramatica.items():
        for elemento in corpo:
            cont = 0
            for letra in elemento:
                if letra not in Gramatica:  # É um terminal
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
                    if letra not in Gramatica:  # Terminal
                        cont += 1
                    elif letra in Geradores:    # Variável que já provou ser geradora
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



def calculaAlcancaveis(Gramatica, Geradores):
    Alc = ["S"]
    AlcTemp = []
    tam = len(Alc)

    while True:
        for cabeca, corpo in Gramatica.items():
            
            if cabeca in Alc and cabeca in Geradores:
                for elemento in corpo:
                    
                   
                    corpo_valido = True
                    for letra in elemento:
                        if letra in Gramatica and letra not in Geradores:
                            corpo_valido = False
                            break
                    
                    # Se a produção for válida, seus componentes tornam-se alcançáveis
                    if corpo_valido:
                        for letra in elemento:
                            if letra in Gramatica:  # Se for uma variável
                                if letra not in Alc and letra not in AlcTemp:
                                    AlcTemp.append(letra)

        Alc.extend(AlcTemp)

        if len(Alc) == tam:
            break
        else:
            tam = len(Alc)
            AlcTemp.clear()

    return Alc


def procuraInuteis(Gramatica):
    # 1. Calcula os geradores primeiro
    Geradores = calculaGeradores(Gramatica)
    
    # 2. Calcula os alcançáveis filtrando os não-geradores
    Alcancaveis = calculaAlcancaveis(Gramatica, Geradores)

    Inuteis = []

    # Um símbolo é inútil se não for gerador OU se não for alcançável
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