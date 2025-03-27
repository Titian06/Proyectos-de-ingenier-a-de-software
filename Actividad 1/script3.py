import time
import os
import re

# Función para extraer y ordenar palabras de un archivo
def extraer_y_ordenar_palabras(filename):
    start_time = time.time()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Leer el contenido del archivo
            # Usar una expresión regular para extraer palabras (incluyendo caracteres especiales como guiones)
            palabras = re.findall(r'\b[\w-]+\b', content)
            # Ordenar las palabras alfabéticamente (ignorando mayúsculas/minúsculas)
            palabras_ordenadas = sorted(palabras, key=lambda x: x.lower())
    except Exception as e:
        print(f"Error al procesar el archivo {filename}: {e}")
        return None, None
    end_time = time.time()
    return palabras_ordenadas, end_time - start_time  # Devolver la lista de palabras ordenadas y el tiempo que tardó

# Función principal
def main():
    # Lista de archivos sin etiquetas HTML (generados en el paso anterior)
    clean_files = [f"clean_{i:03}.html" for i in range(2, 504)]  # Nombres desde clean_002.html hasta clean_503.html
    clean_files.extend(["clean_hard.html", "clean_medium.html", "clean_simple.html"])  # Agrega los otros archivos

    # Archivo de log
    log_file = "a3_matricula.txt"
    total_time = 0  # Tiempo total en procesar todos los archivos

    # Abrir el archivo de log en modo escritura
    with open(log_file, 'w', encoding='utf-8') as log:
        # Recorrer cada archivo sin etiquetas HTML
        for filename in clean_files:
            if os.path.exists(filename):  # Verificar si el archivo existe
                palabras_ordenadas, elapsed_time = extraer_y_ordenar_palabras(filename)  # Extraer y ordenar palabras
                if palabras_ordenadas is not None:
                    # Crear un archivo de salida con la lista de palabras ordenadas
                    output_filename = f"palabras_ordenadas_{filename}"
                    with open(output_filename, 'w', encoding='utf-8') as output_file:
                        for palabra in palabras_ordenadas:
                            output_file.write(f"{palabra}\n")
                    log.write(f"Archivo: {filename}, Tiempo: {elapsed_time:.6f} segundos\n")
                    total_time += elapsed_time
            else:
                log.write(f"Archivo: {filename}, No encontrado\n")

        # Escribir el tiempo total en el archivo de log
        log.write(f"\nTiempo total en procesar todos los archivos: {total_time:.6f} segundos\n")

    print(f"Proceso completado. Revisa el archivo de log: {log_file}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()