from decryptor import decrypt

ciphertext = bytearray(b"=\xf1/\x8a\x06\xda\x99l\xf2P\xad;\xa9\x9a;H\xfc\xa8="
                       b"SU\xdb\x81i\xabJ\xaa\x99\x15}\x02\xde")

BLOCK_LEN = 16

original_ciphertext = ciphertext.copy()
decrypted = bytearray()
for byte in range(1, len(ciphertext) - BLOCK_LEN + 1):
    original_byte = ciphertext[-BLOCK_LEN - byte]

    # Modify known bytes to generate correct PKCS#7 padding.
    for i, decrypted_byte in enumerate(decrypted):
        ciphertext[-BLOCK_LEN - i - 1] = decrypted_byte ^ byte

    # Flip the bits of the preceeding byte to avoid original padding.
    if byte < len(ciphertext) - BLOCK_LEN:
        ciphertext[-BLOCK_LEN - byte - 1] ^= 0xff

    for i in range(256):
        ciphertext[-BLOCK_LEN - byte] = i
        if decrypt(ciphertext):
            # This is the decrypted byte which is XOR-ed with the original
            # ciphertext to get the actual plaintext.
            decrypted.append(i ^ byte)
            break

# We have added decrypted bytes backwards so we have to reverse the list.
decrypted = decrypted[::-1]
for i, mixin in enumerate(original_ciphertext[-2 * BLOCK_LEN : -BLOCK_LEN]):
    # Derive the original plaintext of the message via the ciphertext.
    decrypted[i] = decrypted[i] ^ mixin
print(decrypted)
