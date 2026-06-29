"""
Modulo etapa3_unitarias.py

Verificacao da Etapa 3 da simplificacao de gramaticas: remocao de
producoes unitarias (tambem chamadas de producoes de substituicao
simples ou "chain rules").

Uma producao e unitaria quando tem a forma A -> B, em que B e um
unico simbolo nao-terminal (B esta em N).

Este modulo apenas VERIFICA a condicao; nao realiza a remocao.
"""

from dataclasses import dataclass, field
from typing import List, Set, Tuple

from grammar import Grammar


@dataclass
class ResultadoEtapa3:
    ok: bool
    producoes_unitarias: List[Tuple[str, str]] = field(default_factory=list)

    def relatorio(self) -> str:
        if self.ok:
            return "Etapa 3 OK: a gramatica nao possui producoes unitarias."

        linhas: List[str] = ["Etapa 3 FALHOU: a gramatica possui producoes unitarias."]
        for cabeca, destino in self.producoes_unitarias:
            linhas.append(f"  - {cabeca} -> {destino}")
        return "\n".join(linhas)


def verificar_etapa3(g: Grammar) -> ResultadoEtapa3:
    """Verifica se a gramatica g esta livre de producoes unitarias (A -> B)."""
    encontradas: List[Tuple[str, str]] = []

    for cabeca, corpo in g.all_productions():
        if len(corpo) == 1 and corpo[0] in g.non_terminals:
            encontradas.append((cabeca, corpo[0]))

    ok = len(encontradas) == 0
    return ResultadoEtapa3(ok=ok, producoes_unitarias=encontradas)
