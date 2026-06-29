# Trabalho 2 - LFA 2026.1 - Verificacao das 3 etapas de simplificacao de gramaticas

**Disciplina:** Linguagens Formais e Automatos - 2026.1
**Instituicao:** UTFPR - Campus Ponta Grossa - COCIC
**Professor:** Gleifer Vaz Alves
**Equipe:** <NOME 1>, <NOME 2>
**Tema escolhido:** (c) Implementacao das verificacoes das 3 etapas de simplificacao de gramaticas (apenas a verificacao)

## Descricao

Este projeto implementa tres verificadores independentes, cada um correspondente
a uma das etapas classicas de simplificacao de Gramaticas Livres de Contexto (GLC):

1. **Etapa 1** - Verifica a ausencia de simbolos inuteis (nao-terminais improdutivos
   e simbolos inalcancaveis a partir do simbolo inicial).
2. **Etapa 2** - Verifica a ausencia de producoes vazias (epsilon-producoes), exceto
   pela excecao classica `S -> epsilon` quando aplicavel.
3. **Etapa 3** - Verifica a ausencia de producoes unitarias (producoes de
   substituicao simples, do tipo `A -> B`).

O programa nao realiza a simplificacao da gramatica -- apenas informa, para cada
etapa, se a gramatica de entrada ja satisfaz a condicao correspondente, apontando
os simbolos/producoes responsaveis pela falha quando aplicavel.

## Estrutura do repositorio

```
trabalho-lfa-simplificacao/
├── README.md
├── requirements.txt
├── src/
│   ├── grammar.py            # estrutura de dados da gramatica + parser do arquivo de entrada
│   ├── etapa1_inuteis.py     # verificacao de simbolos inuteis
│   ├── etapa2_vazias.py      # verificacao de producoes vazias
│   ├── etapa3_unitarias.py   # verificacao de producoes unitarias
│   └── main.py                # CLI: carrega a gramatica e roda os 3 verificadores
├── exemplos/                  # gramaticas de exemplo usadas como casos de teste
├── testes/                    # suite de testes automatizados (pytest)
├── docs/                      # relatorio/artigo (fonte e PDF)
└── slides/                    # apresentacao de slides (PDF)
```

## Formato do arquivo de gramatica

```
N: S, A, B
T: a, b
S: S
P:
S -> A B
A -> a
B -> b | epsilon
```

- `N`: lista de nao-terminais, separados por virgula.
- `T`: lista de terminais, separados por virgula.
- `S`: simbolo inicial.
- `P`: uma producao por linha, no formato `CABECA -> corpo`. Alternativas
  da mesma cabeca podem ser separadas por `|`. A cadeia vazia e
  representada pela palavra-chave `epsilon`.

Veja exemplos completos na pasta `exemplos/`.

## Como executar

Requer Python 3.10+.

```bash
cd src
python main.py ../exemplos/gramatica_simplificada.txt
```

Saida esperada (resumida): relatorio de cada etapa (OK ou FALHOU, com a lista
de simbolos/producoes problematicos) e uma conclusao final indicando se a
gramatica esta simplificada.

## Como rodar os testes

```bash
pip install -r requirements.txt
pytest testes/ -v
```

## Casos de teste incluidos

| Arquivo | O que testa |
|---|---|
| `gramatica_simplificada.txt` | Gramatica ja simplificada (passa nas 3 etapas) |
| `gramatica_com_inuteis.txt` | Nao-terminal improdutivo (`C`) e simbolo inalcancavel (`D`) |
| `gramatica_com_vazias.txt` | Producao vazia indevida (`B -> epsilon`) |
| `gramatica_com_unitarias.txt` | Producao unitaria (`S -> A`) |
| `gramatica_excecao_S_vazio.txt` | Caso especial `S -> epsilon` permitido pela etapa 2, mas que ainda falha na etapa 3 (`S -> A`) |

## Uso de ferramentas de IA

> Indicar aqui, conforme exigido pelo enunciado do trabalho, onde e quais
> ferramentas de IA foram utilizadas (por exemplo, no codigo, no relatorio
> e/ou nos slides), incluindo o nome da ferramenta empregada.

## Referencias

> Completar com as referencias bibliograficas utilizadas no relatorio/artigo
> (material de aula, livros de LFA, etc.).
