
def extract_appended_data(jpeg_path, output_path):
    with open(jpeg_path, "rb") as f:
        data = f.read()

    # JPEG EOI marker - 0xFFD9
    eoi_marker = b'\xff\xd9'
    eoi_index = data.find(eoi_marker)

    if eoi_index == -1:
        print("EOI marker not found. Not a valid JPEG or no appended data.")
        return

    # Extract appended data after the EOI marker
    appended_data = data[eoi_index + 2:]  # +2 to skip the EOI itself

    if not appended_data:
        print("No appended data found after EOI marker.")
        return

    # Save appended data to file
    with open(output_path, "wb") as out_file:
        out_file.write(appended_data)

    print(f"Appended data extracted and saved to {output_path}")


extract_appended_data("bonus2.jpg", "appended_data.bin")
