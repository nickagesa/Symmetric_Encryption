# ASymmetric Encryption🔐

Asymmetric encryption, also known as public-key cryptography, uses a pair of keys: a public key to encrypt data and a private key to decrypt it. In learning scenarios, it helps demonstrate how two parties can securely exchange messages by sharing their public keys while keeping their private keys secret. Each sender encrypts messages using the recipient’s public key, ensuring that only the recipient can decrypt them. 
In real-world applications, asymmetric encryption is widely used in securing web traffic (like HTTPS), email encryption, and digital signatures, providing both confidentiality and authenticity in communication over untrusted networks.
## Results
<img src="https://github.com/user-attachments/assets/28069cc8-fbcb-4838-b619-142eabe69a2d" width="450" height="100"/>

*Ref 1: Generated Public Key*

<img src="https://github.com/user-attachments/assets/142d8825-edca-4aa6-96d3-c026788aa42f" width="450" height="200"/>

*Ref 2: Generated Private Key*

<img src="https://github.com/user-attachments/assets/343cadde-e845-4a48-9464-3ffd517bbcc2" width="590" height="310"/>

*Ref 3: Encrypted and decrypted Messages*


## Usage 
1. **Install the cryptography library**
   ```sh
   pip install rsa
   
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








