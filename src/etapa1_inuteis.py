"""
Modulo etapa1_inuteis.py

Verificacao da Etapa 1 da simplificacao de gramaticas: remocao de
simbolos inuteis. Um simbolo e considerado "util" se, e somente se,
ele e PRODUTIVO e ALCANCAVEL ao mesmo tempo.

- Produtivo: o nao-terminal consegue gerar (eventualmente) uma cadeia
  formada apenas por terminais.
- Alcancavel: o simbolo pode ser obtido a partir do simbolo inicial S
  por meio de uma ou mais derivacoes.

Este modulo apenas VERIFICA se a gramatica ja esta livre de simbolos
inuteis -- nao realiza a remocao (conforme pedido no enunciado do
trabalho, tema (c)).
"""

from dataclasses import dataclass, field
from typing import List, Set

from grammar import EPSILON, Grammar


@dataclass
class ResultadoEtapa1:
    ok: bool
    nao_terminais_improdutivos: Set[str] = field(default_factory=set)
    simbolos_inalcancaveis: Set[str] = field(default_factory=set)

    def relatorio(self) -> str:
        if self.ok:
            return "Etapa 1 OK: nao ha simbolos inuteis na gramatica."

        linhas: List[str] = ["Etapa 1 FALHOU: a gramatica possui simbolos inuteis."]
        if self.nao_terminais_improdutivos:
            lista = ", ".join(sorted(self.nao_terminais_improdutivos))
            linhas.append(f"  - Nao-terminais improdutivos: {lista}")
        if self.simbolos_inalcancaveis:
            lista = ", ".join(sorted(self.simbolos_inalcancaveis))
            linhas.append(f"  - Simbolos inalcancaveis a partir de {{S}}: {lista}")
        return "\n".join(linhas)


def calcular_produtivos(g: Grammar) -> Set[str]:
    """
    Calcula o conjunto de nao-terminais produtivos por ponto fixo:
    inicia vazio e adiciona A sempre que existir uma producao
    A -> X1 X2 ... Xn em que todo Xi e terminal ou ja e produtivo
    (ou a producao e A -> epsilon).
    Repete até nao haver mais mudancas.
    """
    produtivos: Set[str] = set()
    mudou = True

    while mudou:
        mudou = False
        for cabeca, corpos in g.productions.items():
            if cabeca in produtivos:
                continue
            for corpo in corpos:
                if corpo == (EPSILON,):
                    produtivos.add(cabeca)
                    mudou = True
                    break
                if all(s in g.terminals or s in produtivos for s in corpo):
                    produtivos.add(cabeca)
                    mudou = True
                    break

    return produtivos


def calcular_alcancaveis(g: Grammar) -> Set[str]:
    """
    Calcula o conjunto de simbolos (terminais e nao-terminais)
    alcancaveis a partir do simbolo inicial S, por ponto fixo:
    inicia com {S} e, para cada nao-terminal ja alcancado, adiciona
    todos os simbolos que aparecem no corpo de suas producoes.
    """
    alcancaveis: Set[str] = {g.start_symbol}
    mudou = True

    while mudou:
        mudou = False
        nao_terminais_alcancados = [s for s in alcancaveis if s in g.non_terminals]
        for nt in nao_terminais_alcancados:
            for corpo in g.productions.get(nt, []):
                for simbolo in corpo:
                    if simbolo == EPSILON:
                        continue
                    if simbolo not in alcancaveis:
                        alcancaveis.add(simbolo)
                        mudou = True

    return alcancaveis


def verificar_etapa1(g: Grammar) -> ResultadoEtapa1:
    """Verifica se a gramatica g esta livre de simbolos inuteis."""
    produtivos = calcular_produtivos(g)
    alcancaveis = calcular_alcancaveis(g)

    nao_terminais_improdutivos = g.non_terminals - produtivos
    simbolos_usados = _simbolos_realmente_usados(g)
    simbolos_inalcancaveis = {s for s in simbolos_usados if s not in alcancaveis}

    ok = (not nao_terminais_improdutivos) and (not simbolos_inalcancaveis)
    return ResultadoEtapa1(
        ok=ok,
        nao_terminais_improdutivos=nao_terminais_improdutivos,
        simbolos_inalcancaveis=simbolos_inalcancaveis,
    )


def _simbolos_realmente_usados(g: Grammar) -> Set[str]:
    """
    Retorna apenas os simbolos que de fato aparecem na gramatica
    (em N, em T, ou no corpo de alguma producao), para nao acusar
    como 'inalcancavel' um simbolo declarado em N ou T mas nunca
    utilizado em nenhuma producao.
    """
    usados: Set[str] = {g.start_symbol}
    for cabeca, corpo in g.all_productions():
        usados.add(cabeca)
        for simbolo in corpo:
            if simbolo != EPSILON:
                usados.add(simbolo)
    return usados
