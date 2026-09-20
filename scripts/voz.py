#!/usr/bin/env python3
"""Diagnóstico quantitativo de voz para ensaios da série.

Uso:  python3 scripts/voz.py ensaios/19_seis-dias-uteis_substack.md

Implementa as métricas da seção 4 do CLAUDE.md. Nenhuma delas é veredito:
são gatilhos de revisão. O objetivo é tornar mecânico o que hoje depende de
alguém contar à mão.
"""

import re
import statistics
import sys
import unicodedata


def carregar(caminho):
    with open(caminho, encoding="utf-8") as fh:
        return fh.read()


def separar_corpo_e_referencias(texto):
    """Corpo = tudo antes da nota de verificação. Referências = seção própria."""
    corpo = texto
    for marcador in ("## Nota de verificação", "## Referências"):
        pos = texto.find(marcador)
        if pos != -1:
            corpo = min(corpo, texto[:pos], key=len)
    m = re.search(r"^##\s*Referências\s*$(.*?)(?=^##\s|\Z)", texto, re.M | re.S)
    referencias = m.group(1) if m else ""
    return corpo, referencias


def limpar(corpo):
    """Remove títulos, itálicos de rubrica, separadores e marcações."""
    linhas = []
    for linha in corpo.splitlines():
        if linha.startswith("#") or linha.strip() in ("---", "-----", ""):
            continue
        if linha.startswith(">"):
            continue
        linhas.append(linha)
    texto = " ".join(linhas)
    texto = re.sub(r"\*+", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def frases(texto):
    bruto = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÚÁÉÍÓÚÂÊÔÃÕÇ])", texto)
    return [f.strip() for f in bruto if len(f.strip()) > 1]


def palavras(frase):
    return [p for p in re.findall(r"[\wÀ-ÿ'-]+", frase) if p]


def comeca_sem_sujeito(frase):
    """Heurística de fragmentação: frase curta abrindo por verbo ou cópula."""
    primeira = palavras(frase)
    if not primeira:
        return False
    p = unicodedata.normalize("NFD", primeira[0].lower())
    p = "".join(c for c in p if unicodedata.category(c) != "Mn")
    gatilhos = {
        "e", "foi", "sao", "era", "eram", "acha", "vira", "serve", "mede",
        "fica", "ficou", "virou", "custa", "tem", "veio", "vem", "sobra",
        "sobrou", "resta", "restou", "nao", "seria", "significa", "descreve",
    }
    return p in gatilhos


def contar_travessoes(texto):
    return texto.count("—")


def contar_molde_nao_e_x_e_y(fs):
    """Molde 'Não é X. É Y.' e variantes coladas, banido por padrão."""
    ocorrencias = []
    padrao_interno = re.compile(
        r"\bN[ãa]o\s+(?:é|foi|era)\b[^.!?]*[.;,]\s*(?:É|Foi|Era)\b", re.I)
    for i, f in enumerate(fs):
        if padrao_interno.search(f):
            ocorrencias.append(f[:90])
            continue
        if i + 1 < len(fs):
            atual = f.strip()
            prox = fs[i + 1].strip()
            if re.match(r"^N[ãa]o\s+(é|foi|era)\b", atual, re.I) and \
               re.match(r"^(É|Foi|Era)\b", prox):
                ocorrencias.append(f"{atual[:60]} | {prox[:40]}")
    return ocorrencias


def referencias_fantasma(corpo, referencias):
    """Sobrenome em MAIÚSCULAS na seção de referências, ausente do corpo."""
    fantasmas = []
    for linha in referencias.splitlines():
        linha = linha.strip()
        if not linha:
            continue
        m = re.match(r"^([A-ZÀ-Ú][A-ZÀ-Ú\s'-]{2,}?),", linha)
        if not m:
            continue
        sobrenome = m.group(1).strip()
        alvo = sobrenome.capitalize()
        if alvo.lower() not in corpo.lower():
            fantasmas.append(sobrenome)
    return fantasmas


def main():
    if len(sys.argv) < 2:
        print("uso: python3 scripts/voz.py <arquivo.md>")
        return 1

    caminho = sys.argv[1]
    texto = carregar(caminho)
    corpo_bruto, referencias = separar_corpo_e_referencias(texto)
    corpo = limpar(corpo_bruto)
    fs = frases(corpo)
    tamanhos = [len(palavras(f)) for f in fs]
    total_palavras = sum(tamanhos)

    media = statistics.mean(tamanhos) if tamanhos else 0
    desvio = statistics.pstdev(tamanhos) if len(tamanhos) > 1 else 0
    curtas = [t for t in tamanhos if t <= 6]
    pct_curtas = 100 * len(curtas) / len(tamanhos) if tamanhos else 0

    travessoes = contar_travessoes(texto)
    teto_travessoes = int(total_palavras * 2 / 500)
    moldes = contar_molde_nao_e_x_e_y(fs)
    fantasmas = referencias_fantasma(corpo, referencias)

    fragmentos = [f for f in fs
                  if len(palavras(f)) <= 6 and comeca_sem_sujeito(f)]

    print(f"arquivo: {caminho}")
    print(f"palavras no corpo: {total_palavras}")
    print(f"frases: {len(fs)}")
    print(f"media / desvio-padrao: {media:.1f} / {desvio:.1f}")
    print(f"frases <= 6 palavras: {pct_curtas:.1f}% ({len(curtas)})")
    print()

    def veredito(ok, rotulo, detalhe=""):
        marca = "OK  " if ok else "REVER"
        print(f"[{marca}] {rotulo}{detalhe}")

    veredito(travessoes <= teto_travessoes,
             "travessoes", f": {travessoes} (teto {teto_travessoes})")
    veredito(not moldes,
             "molde 'Nao e X. E Y.'", f": {len(moldes)}")
    for m in moldes:
        print(f"         > {m}")
    veredito(desvio >= 11.0,
             "desvio-padrao de tamanho de frase",
             f": {desvio:.1f} (alvo >= 11,0)")
    veredito(pct_curtas <= 10.0,
             "proporcao de frases curtissimas",
             f": {pct_curtas:.1f}% (alvo <= 10%)")
    veredito(not fantasmas,
             "referencias fantasma", f": {len(fantasmas)}")
    for f in fantasmas:
        print(f"         > {f}")
    veredito(not fragmentos,
             "candidatos a fragmentacao ilegitima", f": {len(fragmentos)}")
    for f in fragmentos[:12]:
        print(f"         > {f}")

    print()
    print("O par que importa: o desvio-padrao deve SUBIR enquanto a proporcao")
    print("de frases curtissimas CAI. Desvio alto com muitas frases curtas e")
    print("burstiness manufaturada por ponto final em meia oracao.")
    print("Teste manual para cada fragmento acima: a 2a frase sobrevive sozinha?")
    return 0


if __name__ == "__main__":
    sys.exit(main())
