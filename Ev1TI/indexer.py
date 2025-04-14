import os
import sys
from collections import defaultdict

def index(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    posting = defaultdict(list)
    token_set = set()

    for idx, file_name in enumerate(os.listdir(input_dir)):
        if file_name.endswith('.txt'):
            with open(os.path.join(input_dir, file_name), 'r', encoding='utf-8') as f:
                words = f.read().lower().split()
                for word in words:
                    token_set.add(word)
                    posting[word].append(idx)

    with open(os.path.join(output_dir, 'dictionary.txt'), 'w', encoding='utf-8') as f:
        for word in sorted(token_set):
            f.write(word + '\n')

    with open(os.path.join(output_dir, 'posting.txt'), 'w', encoding='utf-8') as f:
        for word in sorted(posting):
            doc_ids = ','.join(map(str, posting[word]))
            f.write(f'{word}: {doc_ids}\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: index input-dir output-dir")
    else:
        index(sys.argv[1], sys.argv[2])