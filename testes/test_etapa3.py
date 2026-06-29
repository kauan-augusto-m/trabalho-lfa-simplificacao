"""
Testes da Etapa 3 (verificacao de producoes unitarias / chain rules).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from grammar import load_grammar
from etapa3_unitarias import verificar_etapa3

EXEMPLOS = os.path.join(os.path.dirname(__file__), "..", "exemplos")


def test_gramatica_simplificada_passa_etapa3():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_simplificada.txt"))
    resultado = verificar_etapa3(g)
    assert resultado.ok is True
    assert resultado.producoes_unitarias == []


def test_gramatica_com_unitarias_falha_etapa3():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_unitarias.txt"))
    resultado = verificar_etapa3(g)
    assert resultado.ok is False
    assert ("S", "A") in resultado.producoes_unitarias


def test_excecao_S_vazio_tem_producao_unitaria():
    # S -> A e unitaria, mesmo que S -> epsilon seja permitido pela etapa 2
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_excecao_S_vazio.txt"))
    resultado = verificar_etapa3(g)
    assert resultado.ok is False
    assert ("S", "A") in resultado.producoes_unitarias
