import os

def generar_indice_documentos():
    ruta_entrada = r"C:\Users\angel\OneDrive\Documentos\Tecmilenio\Proyectos-de-ingenier-a-de-software-main\assets"
    ruta_salida = r"C:\Users\angel\OneDrive\Documentos\Tecmilenio\Proyectos-de-ingenier-a-de-software-main\Fase_4\documentos.txt"
    
    archivos_excluidos = {"hard.html", "medium.html", "simple.html"}
    documentos = []
    contador = 1

    for numero in range(2, 504):
        archivo = f"{numero:03}.html"
        if archivo not in archivos_excluidos:
            documentos.append((contador, archivo))
            contador += 1

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        for doc_id, nombre_archivo in documentos:
            salida.write(f"{doc_id}\t{doc_id}\t{nombre_archivo}\n")

if __name__ == "__main__":
    generar_indice_documentos()
