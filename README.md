# Symmetric Encryption🔐

This is a simple Python project to **encrypt** and **decrypt** files using symmetric encryption with the `cryptography` library's Fernet module.
 
## Results
<img src="https://github.com/user-attachments/assets/6573372c-3f16-4ea2-a473-25ff39619d7f" width="550" height="300"/>

*Ref 1: Original Document*

<img src="https://github.com/user-attachments/assets/c349cf19-edfb-457e-a197-cbc0d5b296e8" width="450" height="100"/>

*Ref 2: Generated Encryption Key*

<img src="https://github.com/user-attachments/assets/179e942c-d02d-414d-95d2-f462160b68f6" width="590" height="310"/>

*Ref 3: Encrypted Document*

<img src="https://github.com/user-attachments/assets/ed1c3618-1cc1-42d1-933d-3e8745f9d9c8" width="550" height="300"/>

*Ref 4: Decrypted Document*

## Usage 
1. **Install the cryptography library**
   ```sh
   pip install cryptography
   
2. **Encrypting a file***
   Run the encryption.py script to encrypt your target file:
   ```sh
   python encryption.py
 This will:
 - Generate an encryption key and save it to key.key.
 - Encrypt the specified file and save it as <filename>.encrypted.
  
3. **Decrypting a file**:
   Run the decryption.py script to decrypt an encrypted file:
   ```sh
   python decryption.py
 This will:
 - Read the encryption key from key.key.
 - Decrypt the encrypted file and save the output.

⚠️ **Important**:
Keep the key.key file safe! Without it, you cannot decrypt your files.

### Notes
- Every time you run encryption.py, a new key is generated. If you want to encrypt multiple files with the same key, save and reuse your key.key.
- Always test decryption to make sure your process works before deleting original files.

## License
This project is open-source and free to use.

Made with ❤️ for learning purposes.








