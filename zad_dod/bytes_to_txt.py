
def bytes_bin_to_txt(input_path, output_path):
    with open(input_path, 'rb') as f:
        data = f.read()

    hex_string = ' '.join(f'{b:02X}' for b in data)

    with open(output_path, 'w') as out_file:
        out_file.write(hex_string)


bytes_bin_to_txt('appended_data.bin', 'appended_data.txt')