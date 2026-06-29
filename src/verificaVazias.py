def printGramatica(gramatica):
    for cabeca, corpo in gramatica.items():
        print(f"{cabeca} {corpo}")
    

def prodVazia(Gramatica):
    Ve = []
    VeTemp = []
    P1 = {}
    
    #Producoes diretamente vazias
    for cabeca, corpo in Gramatica.items():
        if "ε" in corpo:
            Ve.append(cabeca)  
    
    tam = len(Ve)
                
    #Producoes que são vazias indiretamente
    while True:    
        for cabeca, corpo in Gramatica.items():
            for elemento in corpo:
                cont = 0
                for letra in elemento:
                    if letra in Ve:
                        cont = cont + 1
                if cont == len(elemento):
                    if (cabeca not in Ve) and (cabeca not in VeTemp):
                        VeTemp.append(cabeca)
        
        Ve.extend(VeTemp)
        
        #Condicao de parada
        if len(Ve) == tam:
            break
        else:
            tam = len(Ve)
            VeTemp.clear()
    
    for cabeca, corpo in Gramatica.items():
        for elemento in corpo:
            if "ε" not in elemento:
                if cabeca in P1:
                    P1[cabeca].append(elemento)
                else:
                    P1[cabeca] = [elemento]
            
    print("Após remoçao de produções vazias:")
    printGramatica(P1)
    
    P1Temp = {}
    while True:
        alteracao = False
        
        
        for cabeca, corpo in P1.items():
            P1Temp[cabeca] = corpo
        
        for cabeca, corpo in P1Temp.items():
            for elemento in corpo:
                for letra in Ve:
                    for i in range(len(elemento)):
                        if elemento[i] == letra:
                            elementoTemp = elemento[:i] + elemento[i+1:]
                    
                    if (len(elementoTemp) > 0) and (elementoTemp not in corpo):
                        P1[cabeca].append(elementoTemp)
                        alteracao = True
                        
        if not alteracao:
            break
        
    print("\n")
    print("Após remoção de produções que levam à produção vazia:")
    printGramatica(P1)
    return P1

def procuraProdVazia(Gramatica):
    
    GramaticaTemp = {}
    
    for cabeca, corpo in Gramatica.items():
        for elemento in corpo:
            if "ε" in elemento:
                if cabeca in GramaticaTemp:
                    GramaticaTemp[cabeca].append(elemento)
                else:
                    GramaticaTemp[cabeca] = [elemento]
        
    if len(GramaticaTemp) > 0:
        print("\nEssa gramática contem produções vazias:")
        printGramatica(GramaticaTemp)
    else:
        print("\nGramática não contêm produções vazias e está pronta para a próxima fase")
