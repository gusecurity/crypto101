import common

import datetime as dt
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import AES

def process(transaction):
    transaction = bytes.fromhex(transaction)
    decryptor = Cipher(AES(common.key), mode=modes.ECB()).decryptor()
    try:
        transaction = decryptor.update(transaction) + decryptor.finalize()
    except Exception as e:
        sys.exit(f"Invalid transaction {e}")

    # Decode fields of the transaction
    sender        = transaction[  :32]
    amount        = transaction[32:40]
    sender_bank   = transaction[40:48]
    recevier_bank = transaction[48:56]
    timestamp     = transaction[54:64]
    receiver      = transaction[64:  ]

    try:
        # Validate important parts of the transaction.
        sender   = sender.decode()
        receiver = receiver.decode()
        amount = int.from_bytes(amount, "little")
    except ValueError:
        sys.exit("Invalid transaction")

    print(f"{sender} -{amount}-> {receiver}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(f"usage: {sys.argv[0]} <transaction>")
    process(sys.argv[1])

