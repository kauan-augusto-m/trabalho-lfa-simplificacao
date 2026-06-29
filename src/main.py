import verificaVazias
import verificaInuteis

Gramatica = {
    
    "S" : ["AB", "a"],
    "A" : ["B", "ε"],
    "B" : ["b", "ε"],
    "C" : ["cD", "c"],
    "D" : ["dD"],
    "E" : ["aE"]
}

verificaVazias.procuraProdVazia(Gramatica)

Gramatica = verificaVazias.prodVazia(Gramatica)

verificaVazias.procuraProdVazia(Gramatica)

verificaInuteis.procuraInuteis(Gramatica)
