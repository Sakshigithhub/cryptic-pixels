# 🔐 Cryptic Pixels

Cryptic Pixels is a Flask-based web application that encrypts and decrypts image files using the XOR (Exclusive OR) encryption algorithm. It provides a simple and interactive interface where users can upload an image, enter a numeric key, and securely transform the image into an encrypted version. Using the same key, the encrypted image can be restored to its original form.

> **Note:** This project is built for educational purposes to demonstrate the fundamentals of image encryption and XOR-based cryptography.

---

##  Features

* Upload image files through a web interface
* Encrypt images using the XOR algorithm
* Decrypt encrypted images using the same key
* Simple and responsive user interface
* Fast image processing
* Download processed images instantly

---

##  Technologies Used

* Python 3
* Flask
* HTML5
* CSS3
* JavaScript
* Pillow (PIL)

---

##  Project Structure

```
Cryptic-Pixels/
│── app.py
│── requirements.txt
│── static/
│   ├── css/
│   ├── uploads/
│   └── processed/
│── templates/
│   └── index.html
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sakshigithhub/Cryptic-Pixles.git
```

### 2. Navigate to the project folder

```bash
cd Cryptic-Pixles
```

### 3. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📖 How It Works

1. Upload an image.
2. Enter a numeric encryption key.
3. Click **Encrypt** to generate an encrypted image.
4. To restore the original image, upload the encrypted image and use the **same key**.
5. Download the processed image.

---

## 🔒 Encryption Algorithm

This project uses the **XOR (Exclusive OR)** encryption technique.

For every byte of the image:

```
Encrypted Byte = Original Byte XOR Key
```

Since XOR is reversible:

```
Original Byte = Encrypted Byte XOR Same Key
```

Using the same key twice restores the original image.

---

##  Screenshots

### Screenshot 1
![Screenshot 1](screenshots/Screenshot%201.png)

### Screenshot 2
![Screenshot 2](screenshots/Screenshot%202.png)

### Screenshot 3
![Screenshot 3](screenshots/Screenshot%203.png)

### Screenshot 4
![Screenshot 4](screenshots/Screenshot%204.png)



##  Future Improvements

* AES-256 image encryption
* Password-based key generation
* Drag-and-drop image upload
* Multiple image encryption
* Image preview before processing
* Dark mode
* Download history
* File integrity verification (SHA-256)
* User authentication
* Docker deployment

---

##  License

This project is licensed under the MIT License.

---


If you found this project useful, consider giving it a ⭐ on GitHub.
