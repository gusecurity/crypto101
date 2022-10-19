import os
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import AES

# Generate AES key from /dev/urandom (CSRNG)
key = os.urandom(16)
cipher = Cipher(AES(key), mode=modes.ECB())

# Encrypt the following message with the key.
message = b"this is a super secret message"
padding = 32 - len(message)
encryptor = cipher.encryptor()
# Padding is the number of padding bytes.
ciphertext = encryptor.update(message + struct.pack("B", padding) * padding)

# Decrypt the ciphertext with the key.
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)
# Remove the padding
plaintext = plaintext[:-plaintext[-1]]

assert plaintext == message
