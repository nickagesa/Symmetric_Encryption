# decryption.py
# This script decrypts a file that was encrypted using the Fernet symmetric encryption method.

from cryptography.fernet import Fernet

# Paths
key_path = "./key.key" # Path to the key file
encrypted_file_path = "./classified-doc.docx.encrypted" # Path to the encrypted file
decrypted_file_path = "./classified-doc-decrypted.docx" # Path to save the decrypted file

# Function to load the key from a file
def load_key(key_path):
    with open(key_path, "rb") as key_file: # Open the key file in binary mode
        return key_file.read() # Read the key from the file

# Function to decrypt a file
def decrypt_file(encrypted_file_path, output_file_path, fernet_object):
    
    # Open the encrypted file
    with open(encrypted_file_path, "rb") as file: # Open the encrypted file in binary mode
        encrypted_data = file.read() # Read the encrypted data from the file

    decrypted_data = fernet_object.decrypt(encrypted_data) # Decrypt the data using the Fernet object

    # Open the output file to write the decrypted data
    with open(output_file_path, "wb") as file: # Open the output file in binary mode
        file.write(decrypted_data) # Write the decrypted data to the output file

    print(f"File {encrypted_file_path} decrypted successfully to {output_file_path}.")

def main():
    # Load the key
    key = load_key(key_path) # Load the key from the file key_path

    # Create a Fernet object with the key
    fernet_object = Fernet(key) 

    # Decrypt the file
    decrypt_file(encrypted_file_path, decrypted_file_path, fernet_object) # Decrypt the file using the Fernet object

if __name__ == "__main__":
    main() # Call the main function to execute the script
