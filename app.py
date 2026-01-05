from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def xor_encrypt_decrypt(file_path, key):
    """Encrypts or decrypts an image using XOR (Ensures bytes are within range 0-255)."""
    with open(file_path, 'rb') as file:
        image_data = bytearray(file.read())

    # Perform XOR operation while ensuring values remain in the range (0-255)
    for i in range(len(image_data)):
        image_data[i] = (image_data[i] ^ key) % 256  # Fixes ValueError issue

    # Generate encrypted/decrypted file name
    processed_file_path = file_path.replace(".", "_processed.")
    
    with open(processed_file_path, 'wb') as file:
        file.write(image_data)

    return processed_file_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            return "No file uploaded!"

        file = request.files['file']
        key = request.form.get('key')

        if not key.isdigit():
            return "Invalid encryption key!"

        key = int(key) % 256  # Ensure key is within the valid byte range

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Encrypt or decrypt the file
        processed_file = xor_encrypt_decrypt(file_path, key)

        return send_file(processed_file, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
