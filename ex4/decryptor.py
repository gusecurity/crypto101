import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import AES

key = b'\xa1\xb2\x13\xc9|\xe7\xa0\xa6whP\x8d\xa2/\x84k'
iv  = b'[\xda\xc8\xb9\x8c\xc0\x02X@\xf0b\x0b\xbeF\xfe\x89'

cipher = Cipher(AES(key), mode=modes.CBC(iv))
encryptor = cipher.encryptor()
# Encode message with PKCS#7 padding.
message = b"..."
padder = padding.PKCS7(128).padder()
message = padder.update(message) + padder.finalize()
# Output AES encrypted message with CBC padding.
ciphertext = encryptor.update(message) + encryptor.finalize()

def decrypt(ciphertext):
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    try:
        # Remove PKCS#7 padding to get original message.
        unpadder = padding.PKCS7(128).unpadder()
        message = unpadder.update(plaintext) + unpadder.finalize()
    except:
        return False
    return True
