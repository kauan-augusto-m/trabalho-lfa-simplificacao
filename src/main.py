"""
Modulo main.py

Ponto de entrada do programa. Recebe o caminho de um arquivo de
gramatica via linha de comando, carrega a gramatica e executa os
verificadores das 3 etapas de simplificacao, imprimindo o relatorio
de cada uma.

Uso:
    python main.py caminho/para/gramatica.txt
"""

import sys

from grammar import load_grammar
from etapa1_inuteis import verificar_etapa1
from etapa2_vazias import verificar_etapa2
from etapa3_unitarias import verificar_etapa3


def executar(caminho_arquivo: str) -> None:
    g = load_grammar(caminho_arquivo)

    print("=" * 60)
    print(f"Gramatica carregada de: {caminho_arquivo}")
    print("=" * 60)
    print(g)
    print()

    resultado1 = verificar_etapa1(g)
    resultado2 = verificar_etapa2(g)
    resultado3 = verificar_etapa3(g)

    print("-" * 60)
    print(resultado1.relatorio())
    print("-" * 60)
    print(resultado2.relatorio())
    print("-" * 60)
    print(resultado3.relatorio())
    print("-" * 60)

    simplificada = resultado1.ok and resultado2.ok and resultado3.ok
    if simplificada:
        print("\nConclusao: a gramatica esta SIMPLIFICADA (passa nas 3 etapas).")
    else:
        print("\nConclusao: a gramatica NAO esta simplificada.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_para_arquivo_da_gramatica>")
        sys.exit(1)

    executar(sys.argv[1])
