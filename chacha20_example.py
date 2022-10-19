import os
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import ChaCha20

# Generate ChaCha20 key from /dev/urandom (CSRNG)
key    = os.urandom(32)
nonce  = os.urandom(16)
cipher = Cipher(ChaCha20(key, nonce), mode=None)

# Encrypt the following message with the key.
message = b"this is a super secret message"
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message)

# Decrypt the ciphertext with the key.
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)

assert plaintext == message

