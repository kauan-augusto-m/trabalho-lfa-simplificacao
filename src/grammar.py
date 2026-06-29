"""
Modulo grammar.py

Define a estrutura de dados para uma Gramatica Livre de Contexto (GLC)
e a funcao para carrega-la a partir de um arquivo de texto.

Formato de arquivo esperado:

    N: S, A, B, C
    T: a, b
    S: S
    P:
    S -> A B
    A -> a
    B -> b
    C -> a C

Observacoes sobre o formato:
- N: lista de nao-terminais separados por virgula.
- T: lista de terminais separados por virgula.
- S: simbolo inicial.
- P: cada linha seguinte e uma producao no formato "A -> X Y Z".
- Alternativas na mesma producao podem ser separadas por "|",
  ex: "A -> a B | b | epsilon"
- A producao vazia (A deriva a cadeia vazia) e representada pela
  palavra-chave "epsilon" (sem acentos, em minusculo).
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple

EPSILON = "epsilon"  # simbolo usado no arquivo de entrada para representar a cadeia vazia


@dataclass
class Grammar:
    """Representa uma Gramatica Livre de Contexto G = (N, T, P, S)."""

    non_terminals: Set[str] = field(default_factory=set)
    terminals: Set[str] = field(default_factory=set)
    # producoes: mapeia nao-terminal -> lista de "corpos" (cada corpo e uma tupla de simbolos)
    productions: Dict[str, List[Tuple[str, ...]]] = field(default_factory=dict)
    start_symbol: str = ""

    def add_production(self, head: str, body: Tuple[str, ...]) -> None:
        self.productions.setdefault(head, [])
        if body not in self.productions[head]:
            self.productions[head].append(body)

    def all_productions(self):
        """Gera tuplas (cabeca, corpo) para todas as producoes da gramatica."""
        for head, bodies in self.productions.items():
            for body in bodies:
                yield head, body

    def __str__(self) -> str:
        linhas = []
        linhas.append(f"N = {{{', '.join(sorted(self.non_terminals))}}}")
        linhas.append(f"T = {{{', '.join(sorted(self.terminals))}}}")
        linhas.append(f"S = {self.start_symbol}")
        linhas.append("P:")
        for head, bodies in self.productions.items():
            corpos = []
            for body in bodies:
                if body == (EPSILON,):
                    corpos.append("epsilon")
                else:
                    corpos.append(" ".join(body))
            linhas.append(f"  {head} -> {' | '.join(corpos)}")
        return "\n".join(linhas)


def load_grammar(path: str) -> Grammar:
    """Le um arquivo de gramatica no formato descrito no topo deste modulo."""
    g = Grammar()
    modo_producoes = False

    with open(path, "r", encoding="utf-8") as f:
        for linha_bruta in f:
            linha = linha_bruta.strip()

            if not linha or linha.startswith("#"):
                continue  # ignora linhas vazias e comentarios

            if linha.upper().startswith("N:"):
                itens = linha.split(":", 1)[1]
                g.non_terminals = {x.strip() for x in itens.split(",") if x.strip()}
                continue

            if linha.upper().startswith("T:"):
                itens = linha.split(":", 1)[1]
                g.terminals = {x.strip() for x in itens.split(",") if x.strip()}
                continue

            if linha.upper().startswith("S:"):
                g.start_symbol = linha.split(":", 1)[1].strip()
                continue

            if linha.upper().startswith("P:"):
                modo_producoes = True
                continue

            if modo_producoes:
                if "->" not in linha:
                    raise ValueError(f"Linha de producao invalida (sem '->'): {linha}")
                cabeca, corpo_str = linha.split("->", 1)
                cabeca = cabeca.strip()
                alternativas = corpo_str.split("|")
                for alt in alternativas:
                    alt = alt.strip()
                    if alt == "" or alt.lower() == EPSILON:
                        g.add_production(cabeca, (EPSILON,))
                    else:
                        simbolos = tuple(alt.split())
                        g.add_production(cabeca, simbolos)

    _validar_gramatica(g)
    return g


def _validar_gramatica(g: Grammar) -> None:
    """Validacoes basicas para detectar erros de digitacao no arquivo de entrada."""
    if not g.start_symbol:
        raise ValueError("Simbolo inicial (S) nao definido no arquivo.")
    if g.start_symbol not in g.non_terminals:
        raise ValueError(f"Simbolo inicial '{g.start_symbol}' nao esta em N.")

    for cabeca, corpos in g.productions.items():
        if cabeca not in g.non_terminals:
            raise ValueError(f"Producao com cabeca '{cabeca}' fora de N.")
        for corpo in corpos:
            for simbolo in corpo:
                if simbolo == EPSILON:
                    continue
                if simbolo not in g.non_terminals and simbolo not in g.terminals:
                    raise ValueError(
                        f"Simbolo '{simbolo}' usado na producao '{cabeca} -> "
                        f"{' '.join(corpo)}' nao pertence a N nem a T."
                    )
