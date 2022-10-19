import socket

with socket.create_connection(("localhost", 8080)) as s:
    ciphertext = list(s.recv(64))

    # ...
    s.send(bytearray(ciphertext))

    try:
        buf = s.recv(64)
        if b"flag" in buf:
            print(buf)
            break
    except:
        continue
