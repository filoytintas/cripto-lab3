import sys

def process_line(line):
    # Dividir la línea en palabras
    words = line.split()
    processed_words = []
    for word in words:
        # Verificar si la palabra comienza con un número
        if not word[0].isdigit():
            # Transformar la primera letra a mayúscula y agregar un cero al final
            processed_word = word[0].upper() + word[1:] + '0'
            processed_words.append(processed_word)
    # Devolver las palabras procesadas unidas por un espacio
    return ' '.join(processed_words)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            processed_line = process_line(line)
            if processed_line:  # Verificar si la línea procesada no está vacía
                outfile.write(processed_line + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <archivo_entrada> <archivo_salida>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_file(input_file, output_file)
