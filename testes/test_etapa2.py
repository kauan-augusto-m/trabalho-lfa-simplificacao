"""
Testes da Etapa 2 (verificacao de producoes vazias / epsilon-producoes).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from grammar import load_grammar
from etapa2_vazias import verificar_etapa2, calcular_anulaveis

EXEMPLOS = os.path.join(os.path.dirname(__file__), "..", "exemplos")


def test_gramatica_simplificada_passa_etapa2():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_simplificada.txt"))
    resultado = verificar_etapa2(g)
    assert resultado.ok is True
    assert resultado.permitiu_excecao_S is False


def test_gramatica_com_vazias_falha_etapa2():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_vazias.txt"))
    resultado = verificar_etapa2(g)
    assert resultado.ok is False
    assert "B" in resultado.producoes_vazias_indevidas


def test_excecao_S_vazio_e_aceita():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_excecao_S_vazio.txt"))
    resultado = verificar_etapa2(g)
    assert resultado.ok is True
    assert resultado.permitiu_excecao_S is True


def test_calcular_anulaveis_exemplo_vazias():
    g = load_grammar(os.path.join(EXEMPLOS, "gramatica_com_vazias.txt"))
    anulaveis = calcular_anulaveis(g)
    assert "B" in anulaveis
    assert "A" not in anulaveis
    assert "S" not in anulaveis
