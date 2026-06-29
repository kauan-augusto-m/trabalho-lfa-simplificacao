"""
Modulo etapa2_vazias.py

Verificacao da Etapa 2 da simplificacao de gramaticas: remocao de
producoes vazias (epsilon-producoes).

Uma gramatica esta "livre de producoes vazias" se nenhuma producao
tem a forma A -> epsilon, com a unica excecao permitida sendo
S -> epsilon, quando a propria linguagem gerada precisa conter a
cadeia vazia (e, nesse caso, S nao pode aparecer no corpo de
nenhuma outra producao).

Este modulo apenas VERIFICA a condicao; nao realiza a remocao.
"""

from dataclasses import dataclass, field
from typing import List, Set, Tuple

from grammar import EPSILON, Grammar


@dataclass
class ResultadoEtapa2:
    ok: bool
    producoes_vazias_indevidas: Set[str] = field(default_factory=set)
    permitiu_excecao_S: bool = False

    def relatorio(self) -> str:
        if self.ok:
            if self.permitiu_excecao_S:
                return (
                    "Etapa 2 OK: a unica producao vazia e S -> epsilon "
                    "(excecao permitida, pois S nao aparece no corpo de outras producoes)."
                )
            return "Etapa 2 OK: a gramatica nao possui producoes vazias."

        linhas: List[str] = ["Etapa 2 FALHOU: a gramatica possui producoes vazias indevidas."]
        for nt in sorted(self.producoes_vazias_indevidas):
            linhas.append(f"  - {nt} -> epsilon")
        return "\n".join(linhas)


def calcular_anulaveis(g: Grammar) -> Set[str]:
    """
    Calcula o conjunto de nao-terminais anulaveis (que derivam epsilon),
    por ponto fixo: inicia vazio, adiciona A se A -> epsilon e uma
    producao, ou se existe uma producao A -> X1 X2 ... Xn em que todo
    Xi e anulavel.
    """
    anulaveis: Set[str] = set()
    mudou = True

    while mudou:
        mudou = False
        for cabeca, corpos in g.productions.items():
            if cabeca in anulaveis:
                continue
            for corpo in corpos:
                if corpo == (EPSILON,):
                    anulaveis.add(cabeca)
                    mudou = True
                    break
                if corpo and all(s in anulaveis for s in corpo):
                    anulaveis.add(cabeca)
                    mudou = True
                    break

    return anulaveis


def _simbolo_aparece_no_corpo_de_outras_producoes(g: Grammar, simbolo: str) -> bool:
    for cabeca, corpo in g.all_productions():
        if simbolo in corpo:
            return True
    return False


def verificar_etapa2(g: Grammar) -> ResultadoEtapa2:
    """Verifica se a gramatica g esta livre de producoes vazias indevidas."""
    nao_terminais_com_vazia: Set[str] = set()
    for cabeca, corpos in g.productions.items():
        if (EPSILON,) in corpos:
            nao_terminais_com_vazia.add(cabeca)

    if not nao_terminais_com_vazia:
        return ResultadoEtapa2(ok=True)

    # Unica excecao aceitavel: S -> epsilon, e somente se S nao aparece
    # no corpo de nenhuma outra producao da gramatica.
    if nao_terminais_com_vazia == {g.start_symbol}:
        s_aparece_em_corpo = _simbolo_aparece_no_corpo_de_outras_producoes(
            g, g.start_symbol
        )
        if not s_aparece_em_corpo:
            return ResultadoEtapa2(ok=True, permitiu_excecao_S=True)

    producoes_indevidas = nao_terminais_com_vazia - (
        {g.start_symbol} if not _simbolo_aparece_no_corpo_de_outras_producoes(g, g.start_symbol) else set()
    )
    return ResultadoEtapa2(ok=False, producoes_vazias_indevidas=producoes_indevidas)
