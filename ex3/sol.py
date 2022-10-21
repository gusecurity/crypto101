with open("ex3/transactions.txt") as f:
    transactions = [bytes.fromhex(l.strip()) for l in f.readlines()[1::2]]

# ciphertext structure of transaction:
# block 1: sender
# block 2: amount|sender_bank|receiver_bank|timestamp
# block 3: receiver

bob    = transactions[0][64:  ]
eve    = transactions[1][  :32]
amount = transactions[0][32:64]

transaction = bob + amount + eve
print(transaction.hex())

