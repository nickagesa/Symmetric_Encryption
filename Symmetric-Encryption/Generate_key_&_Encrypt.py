# This script encrypts a file using symmetric key and saves the encrypted file to a specified location. 
# It uses the Fernet symmetric encryption method from the cryptography library.
# pip install cryptography

# Import necessary libraries
from cryptography.fernet import Fernet 

key = Fernet.generate_key()  # Generate a new key for encryption

# This key is generated randomly and stored in your system's memory (i.e., in the variable `key`).
# This key is used to encrypt and decrypt the file.
# In a real-world application, you would want to securely store this key for later decryption.
# For example, you could save it to a file or a secure vault.
# Keep in mind that everytime you run this script, a new key will be generated. 
# So, if you want to decrypt the file later, you need to save this key somewhere safe.

# Save the key to a file for later use
with open("key.key", "wb") as key_file: # wb means write in binary mode
    key_file.write(key)  

fernet_object = Fernet(key)  # Create a Fernet object with the generated key
# This object will be used to encrypt and decrypt the file.
# The Fernet object is initialized with the key that was generated earlier.

file_path = "./classified-doc.docx"  # Path to the file you want to encrypt

# Encrypt the file
def encrypt_file(file_path, fernet_object):
    with open(file_path, "rb") as file:  # Open the file in binary mode
        file_data = file.read()  # Read the file data

    encrypted_data = fernet_object.encrypt(file_data)  # Encrypt the file data

    with open(file_path + ".encrypted", "wb") as file:  # Save the encrypted data to a new file
        file.write(encrypted_data)  # Write the encrypted data to the new file

    print(f"File {file_path} encrypted successfully.")


# Call the function to encrypt the file
encrypt_file(file_path, fernet_object)