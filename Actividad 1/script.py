import time
import os

# Función para abrir un archivo y medir el tiempo que tarda
def open_file(filename):
    start_time = time.time()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Leer el contenido del archivo
    except Exception as e:
        print(f"Error al abrir el archivo {filename}: {e}")
        return None
    end_time = time.time()
    return end_time - start_time  # Devolver el tiempo que tardó en abrir el archivo

# Función principal
def main():
    # Lista de archivos HTML
    html_files = [f"{i:03}.html" for i in range(2, 504)]  # Genera nombres desde 002.html hasta 503.html
    html_files.extend(["hard.html", "medium.html", "simple.html"])  # Agrega los otros archivos

    # Archivo de log
    log_file = "a1_matricula.txt"
    total_time = 0  # Tiempo total en abrir todos los archivos

    # Abrir el archivo de log en modo escritura
    with open(log_file, 'w', encoding='utf-8') as log:
        # Recorrer cada archivo HTML
        for filename in html_files:
            if os.path.exists(filename):  # Verificar si el archivo existe
                elapsed_time = open_file(filename)  # Abrir el archivo y medir el tiempo
                if elapsed_time is not None:
                    log.write(f"Archivo: {filename}, Tiempo: {elapsed_time:.6f} segundos\n")
                    total_time += elapsed_time
            else:
                log.write(f"Archivo: {filename}, No encontrado\n")

        # Escribir el tiempo total en el archivo de log
        log.write(f"\nTiempo total en abrir todos los archivos: {total_time:.6f} segundos\n")

    print(f"Proceso completado. Revisa el archivo de log: {log_file}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()