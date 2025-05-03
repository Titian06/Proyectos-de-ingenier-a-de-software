import os
import time
from collections import Counter

CARPETA_HTML = r"C:\Users\angel\OneDrive\Documentos\Tecmilenio\Proyectos-de-ingenier-a-de-software-main\assets"
CARPETA_LOG = r"C:\Users\angel\OneDrive\Documentos\Tecmilenio\Proyectos-de-ingenier-a-de-software-main\Fase_4"
ARCHIVO_LOG = os.path.join(CARPETA_LOG, "a12_A03018750.txt") 

def procesar_documento(nombre_archivo):
    ruta = os.path.join(CARPETA_HTML, nombre_archivo)
    
    inicio = time.time()
    try:
        with open(ruta, encoding="utf-8") as archivo:
            texto = archivo.read()
            palabras = texto.split()

        if not palabras:
            return 0.0, 0.0  # peso, tiempo

        contador = Counter(palabras)
        total_palabras = len(palabras)

        # Calcular peso: TF promedio de tokens únicos
        peso_total = sum((frecuencia / total_palabras) * 100 for frecuencia in contador.values())
        peso_redondeado = round(peso_total, 4)

        fin = time.time()
        duracion = round(fin - inicio, 4)

        return peso_redondeado, duracion

    except Exception as e:
        return 0.0, 0.0

def registrar_log(nombre_archivo, peso, duracion):
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as log:
        log.write(f"Archivo: {nombre_archivo} | Peso: {peso} | Tiempo: {duracion} segundos\n")

def main():
    archivos = [f"{i:03}.html" for i in range(2, 504)
                if f"{i:03}.html" not in {"hard.html", "medium.html", "simple.html"}]

    for archivo in archivos:
        peso, tiempo = procesar_documento(archivo)
        registrar_log(archivo, peso, tiempo)

if __name__ == "__main__":
    main()
