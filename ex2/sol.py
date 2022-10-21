import socket
from random import randint

N_REQUESTS = 2_000

for i in range(N_REQUESTS):
    with socket.create_connection(("localhost", 8080)) as s:
        ciphertext = list(s.recv(64))
        for _ in range(randint(0, 5)):
            ciphertext[randint(0, len(ciphertext) - 1)] ^= 1 << randint(0, 7)
        s.send(bytearray(ciphertext))

        try:
            buf = s.recv(64)
            if b"flag" in buf:
                print(buf)
                break
        except:
            continue

