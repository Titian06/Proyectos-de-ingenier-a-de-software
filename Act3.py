import time
import os
from collections import defaultdict

# Función para extraer palabras de un archivo
def extraer_palabras(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            palabras = re.findall(r'\b[\w-]+\b', content)
            palabras = [palabra.lower() for palabra in palabras]
    except Exception as e:
        print(f"Error al procesar el archivo {filename}: {e}")
        return None
    return palabras

# Función principal
def main(input_dir, output_dir):
    archivos = ["simple.html", "medium.html", "hard.html", "49.html"]
    log_file = os.path.join(output_dir, "a7_matricula.txt")
    total_time = 0

    frecuencia_palabras = defaultdict(int)
    archivos_con_token = defaultdict(set)
    posting_data = []

    with open(log_file, 'w', encoding='utf-8') as log:
        start_total_time = time.time()

        for archivo in archivos:
            input_file = os.path.join(input_dir, archivo)
            if os.path.exists(input_file):
                start_time = time.time()
                palabras = extraer_palabras(input_file)
                if palabras:
                    for palabra in palabras:
                        frecuencia_palabras[palabra] += 1
                        archivos_con_token[palabra].add(archivo)
                    elapsed_time = time.time() - start_time
                    log.write(f"Archivo: {archivo}, Tiempo: {elapsed_time:.6f} segundos\n")
                    total_time += elapsed_time
                else:
                    log.write(f"Archivo: {archivo}, No encontrado\n")

        # Crear el archivo de diccionario
        start_alpha_time = time.time()
        output_alpha = os.path.join(output_dir, "diccionario.txt")
        with open(output_alpha, 'w', encoding='utf-8') as file:
            file.write("Token\tNúmero de documentos\tPosición del primer registro\n")
            posicion = 0
            for palabra, freq in frecuencia_palabras.items():
                num_archivos = len(archivos_con_token[palabra])
                file.write(f"{palabra}\t{num_archivos}\t{posicion}\n")
                posicion += num_archivos

        alpha_time = time.time() - start_alpha_time

        # Crear el archivo de posting
        start_posting_time = time.time()
        output_posting = os.path.join(output_dir, "posting.txt")
        with open(output_posting, 'w', encoding='utf-8') as file:
            file.write("Nombre del archivo\tFrecuencia\n")
            for palabra, archivos in archivos_con_token.items():
                for archivo in archivos:
                    file.write(f"{archivo}\t{frecuencia_palabras[palabra]}\n")

        posting_time = time.time() - start_posting_time

        # Calcular el tiempo total del proceso
        total_process_time = time.time() - start_total_time

        # Escribir el tiempo total en el archivo de log
        log.write(f"Tiempo total en procesar todos los archivos: {total_time:.6f} segundos\n")
        log.write(f"Tiempo en generar el archivo de diccionario: {alpha_time:.6f} segundos\n")
        log.write(f"Tiempo en generar el archivo de posting: {posting_time:.6f} segundos\n")
        log.write(f"Tiempo total del proceso completo: {total_process_time:.6f} segundos\n")

    print(f"Proceso completado. Revisa el archivo de log: {log_file}")
    print(f"Archivo de diccionario generado: {output_alpha}")
    print(f"Archivo de posting generado: {output_posting}")

# Ejecutar la función principal
if __name__ == "__main__":
    input_dir = "C:/Users/JAIME/Downloads/Files"  # Ruta de entrada (donde están los archivos)
    output_dir = "C:/Users/JAIME/Downloads/Files/output"  # Ruta de salida
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    main(input_dir, output_dir)