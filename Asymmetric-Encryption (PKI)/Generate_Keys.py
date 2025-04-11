# Asymmetric encryption
# This code demonstrates the use of asymmetric encryption using the RSA algorithm.
# It generates a pair of public and private keys, encrypts a message with the public key,
# and decrypts it with the private key. The code also includes a function to sign a message
# with the private key and verify the signature with the public key.
# pip install rsa

import rsa

# Generate a pair of public and private keys
(public_key, private_key) = rsa.newkeys(1024) # 1024 bits is a common key size for RSA

# Note: The key size can be increased for more security, but it will also increase the time taken to encrypt and decrypt messages.
# This would generate a public key and private key pair every time you run the code.

# save the keys to files
with open('public_key.pem', 'wb') as f:
    f.write(public_key.save_pkcs1(format='PEM')) # Public key in PEM format

with open('private_key.pem', 'wb') as f:
    f.write(private_key.save_pkcs1(format='PEM')) # Private key in PEM format

# pkcs1 is a standard for public key cryptography
# PEM is a base64 encoded format for storing keys

# Keep the keys in a secure location and do not share the private key with anyone.
# The public key can be shared with anyone to encrypt messages.



