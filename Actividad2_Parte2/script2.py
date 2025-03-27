import time
import os
import re
import sys
from collections import defaultdict

# Función para extraer palabras de un archivo
def extraer_palabras(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Leer el contenido del archivo
            # Usar una expresión regular para extraer palabras (incluyendo caracteres especiales como guiones)
            palabras = re.findall(r'\b[\w-]+\b', content)
            # Convertir todas las palabras a minúsculas
            palabras = [palabra.lower() for palabra in palabras]
    except Exception as e:
        print(f"Error al procesar el archivo {filename}: {e}")
        return None
    return palabras

# Función para tokenizar un archivo y guardar el resultado
def tokenizar_archivo(input_file, output_dir):
    palabras = extraer_palabras(input_file)
    if palabras is not None:
        output_file = os.path.join(output_dir, f"tokenized_{os.path.basename(input_file)}")
        with open(output_file, 'w', encoding='utf-8') as file:
            for palabra in palabras:
                file.write(f"{palabra}\n")
        return palabras
    return []

# Función principal
def main(input_dir, output_dir):
    # Archivos a tokenizar
    archivos = ["simple.html", "medium.html", "hard.html", "49.html"]

    # Archivo de log
    log_file = os.path.join(output_dir, "a5_matricula.txt")
    total_time = 0  # Tiempo total en procesar todos los archivos

    # Diccionario para almacenar la frecuencia de todas las palabras
    frecuencia_palabras = defaultdict(int)

    # Abrir el archivo de log en modo escritura
    with open(log_file, 'w', encoding='utf-8') as log:
        start_total_time = time.time()  # Iniciar el cronómetro para el tiempo total

        # Recorrer cada archivo a tokenizar
        for archivo in archivos:
            input_file = os.path.join(input_dir, archivo)
            print(f"Buscando archivo: {input_file}")  # Línea de depuración
            if os.path.exists(input_file):  # Verificar si el archivo existe
                start_time = time.time()  # Iniciar el cronómetro para el archivo actual
                palabras = tokenizar_archivo(input_file, output_dir)  # Tokenizar el archivo
                if palabras:
                    for palabra in palabras:
                        frecuencia_palabras[palabra] += 1  # Actualizar la frecuencia de las palabras
                    elapsed_time = time.time() - start_time  # Calcular el tiempo que tardó en procesar el archivo
                    log.write(f"Archivo: {archivo}, Tiempo: {elapsed_time:.6f} segundos\n")
                    total_time += elapsed_time
            else:
                log.write(f"Archivo: {archivo}, No encontrado\n")

        # Crear el archivo consolidado ordenado alfabéticamente
        start_alpha_time = time.time()
        palabras_ordenadas_alpha = sorted(frecuencia_palabras.items(), key=lambda x: x[0])
        alpha_time = time.time() - start_alpha_time

        output_alpha = os.path.join(output_dir, "consolidado_alfabetico.txt")
        with open(output_alpha, 'w', encoding='utf-8') as file:
            for palabra, freq in palabras_ordenadas_alpha:
                file.write(f"{palabra} {freq}\n")

        # Calcular el tiempo total del proceso
        total_process_time = time.time() - start_total_time

        # Escribir el tiempo total en el archivo de log
        log.write(f"\nTiempo total en procesar todos los archivos: {total_time:.6f} segundos\n")
        log.write(f"Tiempo en ordenar alfabéticamente: {alpha_time:.6f} segundos\n")
        log.write(f"Tiempo total del proceso completo: {total_process_time:.6f} segundos\n")

    print(f"Proceso completado. Revisa el archivo de log: {log_file}")
    print(f"Archivo consolidado generado: {output_alpha}")

# Ejecutar la función principal
if __name__ == "__main__":
    input_dir = "C:\\Users\\angel\\Downloads\\Files"  # Ruta fija de entrada (donde están los archivos)
    output_dir = "C:\\Users\\angel\\Downloads\\Files\\output"  # Ruta fija de salida
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    main(input_dir, output_dir)