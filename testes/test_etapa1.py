"""
Testes da Etapa 1 (verificacao de simbolos inuteis).

Para executar (a partir da raiz do projeto):
    cd src
    pytest ../testes/test_etapa1.py -v
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from grammar import load_grammar
from etapa1_inuteis import verificar_etapa1, calcular_produtivos, calcular_alcancaveis

EXEMPLOS = os.path.join(os.path.dirname(__file__), "..", "exemplos")


def test_gramatica_simplificada_passa_etapa1():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_simplificada.txt"))
    resultado = verificar_etapa1(g)
    assert resultado.ok is True
    assert resultado.nao_terminais_improdutivos == set()
    assert resultado.simbolos_inalcancaveis == set()


def test_gramatica_com_inuteis_falha_etapa1():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_inuteis.txt"))
    resultado = verificar_etapa1(g)
    assert resultado.ok is False
    assert "C" in resultado.nao_terminais_improdutivos
    assert "C" in resultado.simbolos_inalcancaveis
    assert "D" in resultado.simbolos_inalcancaveis


def test_calcular_produtivos_exemplo_inuteis():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_inuteis.txt"))
    produtivos = calcular_produtivos(g)
    # A, B, D produzem cadeias de terminais; C nunca produz so terminais
    assert produtivos == {"A", "B", "D", "S"}


def test_calcular_alcancaveis_exemplo_inuteis():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_inuteis.txt"))
    alcancaveis = calcular_alcancaveis(g)
    # A partir de S, alcancamos S, A, B, a, b -- nunca C ou D
    assert "C" not in alcancaveis
    assert "D" not in alcancaveis
    assert {"S", "A", "B", "a", "b"}.issubset(alcancaveis)


def test_gramatica_com_unitarias_passa_etapa1():
    # Essa gramatica nao tem problema de simbolos inuteis, so de producao unitaria
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_unitarias.txt"))
    resultado = verificar_etapa1(g)
    assert resultado.ok is True
