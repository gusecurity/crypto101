import common

import datetime as dt
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import AES

def transfer(sender, amount, receiver):
    try:
        # Obtain banking information for involved parties.
        sender, sender_bank = common.accounts[sender.upper()]
        receiver, receiver_bank = common.accounts[receiver.upper()]
        amount = int(amount)
    except (KeyError, ValueError):
        sys.exit("Invalid parameters!")

    # Generate a transaction timestamp.
    timestamp = int(dt.datetime.now().timestamp())

    encryptor = Cipher(AES(common.key), mode=modes.ECB()).encryptor()
    msg  = encryptor.update(sender.encode())
    # Encode: amount|sender_bank|receiver_bank|timestamp
    msg += encryptor.update(amount.to_bytes(8, "little"))
    msg += encryptor.update((sender_bank + receiver_bank).encode())
    msg += encryptor.update(timestamp.to_bytes(8, "little"))
    msg += encryptor.update(receiver.encode())
    msg += encryptor.finalize()
    print(msg.hex())

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(f"usage: {sys.argv[0]} <sender> <amount> <receiver>")
    transfer(*sys.argv[1:])
