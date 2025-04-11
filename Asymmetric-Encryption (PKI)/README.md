# ASymmetric Encryption🔐

Asymmetric encryption, also known as public-key cryptography, uses a pair of keys: a public key to encrypt data and a private key to decrypt it. In learning scenarios, it helps demonstrate how two parties can securely exchange messages by sharing their public keys while keeping their private keys secret. Each sender encrypts messages using the recipient’s public key, ensuring that only the recipient can decrypt them. 

Simple Example:
Let’s say it’s you and Alice.
- You give Alice your public key — so she can encrypt messages to you.
- Alice gives you her public key — so you can encrypt messages to her.

✅ This way, both sides can securely send encrypted messages to each other.

In real-world applications, asymmetric encryption is widely used in securing web traffic (like HTTPS), email encryption, and digital signatures, providing both confidentiality and authenticity in communication over untrusted networks.

## Results
<img src="https://github.com/user-attachments/assets/28069cc8-fbcb-4838-b619-142eabe69a2d" width="400" height="150"/>

*Ref 1: Generated Public Key*

<img src="https://github.com/user-attachments/assets/142d8825-edca-4aa6-96d3-c026788aa42f" width="450" height="300"/>

*Ref 2: Generated Private Key*

<img src="https://github.com/user-attachments/assets/343cadde-e845-4a48-9464-3ffd517bbcc2" width="620" height="100"/>

*Ref 3: Encrypted and decrypted Messages*


## Usage 
1. **Install the cryptography library**
   ```sh
   pip install rsa
   
2. **Generate Public & Private Keys***
   ```sh
   python Generate_Keys.py
 This will:
 - Generate encryption keys and save them as public_key.pem & private_key.pem.
 - Your private key is secreat but you can share your public key.
  
3. **Encrypt & Decrypt a message**:
   ```sh
   python Encrypt_&_Decrypt_Message.py
 This will:
 - Load both keys, use the public key to encrypt & private to decrypt message.
 

⚠️ **Important**:
Keep the private_key.pem file safe! Without it, you cannot decrypt your files.

### Notes
- Every time you run Generate_Keys.py, 2 new key are generated. If you want to encrypt multiple files with the same key, save and reuse your public_key.pem & private_key.pem.

## License
This project is open-source and free to use.

Made with ❤️ for learning purposes.








