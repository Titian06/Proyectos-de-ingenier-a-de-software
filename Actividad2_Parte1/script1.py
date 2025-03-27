import time
import os
import re

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

# Función principal
def main():
    # Lista de archivos con palabras ordenadas (generados en el paso anterior)
    palabras_files = [f"palabras_ordenadas_clean_{i:03}.html" for i in range(2, 504)]  # Nombres desde palabras_ordenadas_clean_002.html hasta palabras_ordenadas_clean_503.html
    palabras_files.extend(["palabras_ordenadas_clean_hard.html", "palabras_ordenadas_clean_medium.html", "palabras_ordenadas_clean_simple.html"])  # Agrega los otros archivos

    # Archivo de log
    log_file = "a4_matricula.txt"
    total_time = 0  # Tiempo total en procesar todos los archivos

    # Lista consolidada de palabras
    palabras_consolidadas = []

    # Abrir el archivo de log en modo escritura
    with open(log_file, 'w', encoding='utf-8') as log:
        start_total_time = time.time()  # Iniciar el cronómetro para el tiempo total

        # Recorrer cada archivo con palabras ordenadas
        for filename in palabras_files:
            if os.path.exists(filename):  # Verificar si el archivo existe
                start_time = time.time()  # Iniciar el cronómetro para el archivo actual
                palabras = extraer_palabras(filename)  # Extraer palabras del archivo
                if palabras is not None:
                    palabras_consolidadas.extend(palabras)  # Agregar palabras a la lista consolidada
                    elapsed_time = time.time() - start_time  # Calcular el tiempo que tardó en procesar el archivo
                    log.write(f"Archivo: {filename}, Tiempo: {elapsed_time:.6f} segundos\n")
                    total_time += elapsed_time
            else:
                log.write(f"Archivo: {filename}, No encontrado\n")

        # Ordenar la lista consolidada de palabras alfabéticamente
        start_sort_time = time.time()
        palabras_consolidadas.sort()
        sort_time = time.time() - start_sort_time

        # Crear el archivo consolidado
        output_filename = "palabras_consolidadas.txt"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for palabra in palabras_consolidadas:
                output_file.write(f"{palabra}\n")

        # Calcular el tiempo total del proceso
        total_process_time = time.time() - start_total_time

        # Escribir el tiempo total en el archivo de log
        log.write(f"\nTiempo total en procesar todos los archivos: {total_time:.6f} segundos\n")
        log.write(f"Tiempo en ordenar la lista consolidada: {sort_time:.6f} segundos\n")
        log.write(f"Tiempo total del proceso completo: {total_process_time:.6f} segundos\n")

    print(f"Proceso completado. Revisa el archivo de log: {log_file}")
    print(f"Archivo consolidado generado: {output_filename}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()