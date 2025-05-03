import os
import time
from collections import defaultdict

CARPETA_FASE4 = r"C:\Users\angel\OneDrive\Documentos\Tecmilenio\Proyectos-de-ingenier-a-de-software-main\Fase_4"
DICCIONARIO = os.path.join(CARPETA_FASE4, "diccionario.txt")
POSTING = os.path.join(CARPETA_FASE4, "posting.txt")
DOCUMENTOS = os.path.join(CARPETA_FASE4, "documentos.txt")
LOG = os.path.join(CARPETA_FASE4, "a13_A03018750.txt") 


def buscar_posicion_en_diccionario(token_buscado):
    with open(DICCIONARIO, encoding="utf-8") as dic:
        for linea in dic:
            partes = linea.strip().split()
            if len(partes) < 2:
                continue
            token, posicion = partes[0], partes[1]
            if token.lower() == token_buscado.lower():
                return int(posicion)
    return None

def buscar_documentos_por_token(token):
    posicion = buscar_posicion_en_diccionario(token)
    if posicion is None:
        return []

    resultados = []
    with open(POSTING, encoding="utf-8") as post:
        for idx, linea in enumerate(post):
            if idx < posicion:
                continue
            if not linea.strip():
                break
            partes = linea.strip().split()
            if len(partes) < 3:
                continue
            token_id, doc_id, peso = partes
            resultados.append((int(doc_id), float(peso)))
    return resultados

def obtener_nombre_documento(doc_id):
    with open(DOCUMENTOS, encoding="utf-8") as doc_file:
        for linea in doc_file:
            partes = linea.strip().split()
            if len(partes) < 3:
                continue
            if partes[0] == str(doc_id):
                return partes[2]
    return f"doc_{doc_id}.html"

def buscar_tokens(tokens):
    inicio = time.time()
    puntajes = defaultdict(float)

    for token in tokens:
        ocurrencias = buscar_documentos_por_token(token)
        for doc_id, peso in ocurrencias:
            puntajes[doc_id] += peso

    resultados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)[:10]
    fin = time.time()

    # Mostrar resultados
    print("\nTop documentos relevantes:")
    for i, (doc_id, puntaje) in enumerate(resultados, 1):
        nombre = obtener_nombre_documento(doc_id)
        print(f"{i}. {nombre} (Puntaje: {round(puntaje, 4)})")

    # Guardar log
    with open(LOG, "a", encoding="utf-8") as log:
        log.write(f"Tokens buscados: {' '.join(tokens)}\n")
        log.write(f"Tiempo de búsqueda: {round(fin - inicio, 4)} segundos\n")
        log.write(f"Top resultados:\n")
        for i, (doc_id, puntaje) in enumerate(resultados, 1):
            nombre = obtener_nombre_documento(doc_id)
            log.write(f"{i}. {nombre} (Puntaje: {round(puntaje, 4)})\n")
        log.write("\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 10:
        print("Uso: python retrieve.py token1 token2 ...")
    else:
        buscar_tokens(sys.argv[1:])
