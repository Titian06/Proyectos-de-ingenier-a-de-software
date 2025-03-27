import time
import os
import re

# Función para eliminar etiquetas HTML de un archivo
def remove_html_tags(filename):
    start_time = time.time()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Leer el contenido del archivo
            # Usar una expresión regular para eliminar las etiquetas HTML
            clean_content = re.sub(r'<[^>]+>', '', content)
    except Exception as e:
        print(f"Error al procesar el archivo {filename}: {e}")
        return None, None
    end_time = time.time()
    return clean_content, end_time - start_time  # Devolver el contenido limpio y el tiempo que tardó

# Función principal
def main():
    # Lista de archivos HTML
    html_files = [f"{i:03}.html" for i in range(2, 504)]  # Genera nombres desde 002.html hasta 503.html
    html_files.extend(["hard.html", "medium.html", "simple.html"])  # Agrega los otros archivos

    # Archivo de log
    log_file = "a2_matricula.txt"
    total_time = 0  # Tiempo total en procesar todos los archivos

    # Abrir el archivo de log en modo escritura
    with open(log_file, 'w', encoding='utf-8') as log:
        # Recorrer cada archivo HTML
        for filename in html_files:
            if os.path.exists(filename):  # Verificar si el archivo existe
                clean_content, elapsed_time = remove_html_tags(filename)  # Eliminar etiquetas y medir el tiempo
                if clean_content is not None:
                    # Crear un archivo de salida sin etiquetas HTML
                    output_filename = f"clean_{filename}"
                    with open(output_filename, 'w', encoding='utf-8') as output_file:
                        output_file.write(clean_content)
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