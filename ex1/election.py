import os
import random
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import AES

N_PARTICIPANTS = 10

# randomly generate AES key from /dev/urandom (CSPRNG)
key = os.urandom(16)
encryptor = Cipher(AES(key), mode=modes.ECB()).encryptor()

for participant in range(N_PARTICIPANTS):
    # candidate is either 'A' or 'B' with fixed probability
    candidate = random.choices('AB', weights=[0.4, 0.6])[0]
    ciphertext = encryptor.update(candidate.encode() + b"\0"*63)

    # "send" the ciphertext to the election server
    print(participant, candidate, ciphertext.hex()[:64], "...")
