import os
import time
import shutil
import subprocess

doc_counts = [10, 20, 30, 40, 50]

with open("tiempos_tokenizacion.txt", "w", encoding="utf-8") as f_token, \
     open("tiempos_indexacion.txt", "w", encoding="utf-8") as f_index:

    for count in doc_counts:
        input_dir = "input-docs"
        temp_dir = "temp-input"
        output_dir = "output"

        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        docs = sorted([f for f in os.listdir(input_dir) if f.endswith(".txt")])[:count]

        for doc in docs:
            shutil.copy(os.path.join(input_dir, doc), os.path.join(temp_dir, doc))

        # Tokenización
        start = time.time()
        subprocess.run(["python", "tokenizer.py", temp_dir, output_dir])
        end = time.time()
        token_time = end - start
        f_token.write(f"Cantidad de documentos: {count}, Tiempo: {token_time:.4f} segundos\n")

        # Indexación
        start = time.time()
        subprocess.run(["python", "indexer.py", temp_dir, output_dir])
        end = time.time()
        index_time = end - start
        f_index.write(f"Cantidad de documentos: {count}, Tiempo: {index_time:.4f} segundos\n")

        print(f"Documentos: {count} → Token: {token_time:.4f}s | Index: {index_time:.4f}s")
