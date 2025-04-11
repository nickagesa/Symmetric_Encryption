import rsa

# Load the public key from a file to encrypt a message
with open('public_key.pem', 'rb') as f:
    public_key_data = rsa.PublicKey.load_pkcs1(f.read())

# Encrypt a message 
message = b'This is a secret message.' # The message must be in bytes format (b'...')
encrypted_message = rsa.encrypt(message, public_key_data) # Encrypt the message with the public key
print(f'Encrypted message: {encrypted_message}\t') # Print the encrypted message

# you can also encrypt the file like this:
# Version 1:
# message = "This is a secret message." 
# encrypted_message = rsa.encrypt(message.encode('utf-8'), public_key_data) 
# encode('utf-8') converts the string to bytes

# Version 2: Encrypt a file using the public key
# with open('message.txt', 'rb') as f:
#     message = f.read() # Read the message from the file
#     encrypted_message = rsa.encrypt(message, public_key_data) # Encrypt the message with the public key

# load the private key from a file to decrypt the message
with open('private_key.pem', 'rb') as f:
    private_key_data = rsa.PrivateKey.load_pkcs1(f.read())


# Decrypt the message with the private key
decrypted_message = rsa.decrypt(encrypted_message, private_key_data) 
print(f'Decrypted message: {decrypted_message.decode("utf-8")}') # Print the decrypted message

