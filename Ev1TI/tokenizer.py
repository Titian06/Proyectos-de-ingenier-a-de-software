import os
import re
import sys

def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens

def main(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    all_tokens = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.txt'):
            with open(os.path.join(input_dir, file_name), 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = tokenize(text)
                all_tokens.extend(tokens)

    with open(os.path.join(output_dir, 'tokens.txt'), 'w', encoding='utf-8') as f:
        for token in all_tokens:
            f.write(token + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: tokenize input-dir output-dir")
    else:
        main(sys.argv[1], sys.argv[2])