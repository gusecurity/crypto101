# Embedded AES key for encrypting all transactions.
key = b"S\xb6\x8b\xf3\xec\x88\x15\xfa\xb0\xca\xd2\xda\xf6c\x15\x94"

# Mapping from customer name to account identifier and associated bank.
accounts = {
    # How convenient that we have 8 byte bank names ;)
    "ALICE": ("809065a294c144f495deaa3c78845ea6", "Barcleys"),
    "BOB":   ("c725e36099be402e8c0d157a3d13a11d", "Revolut "),
    "EVE":   ("f26d8a96f4cf4535a740732a9b056585", "Revolut "),
}

