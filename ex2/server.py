import datetime as dt
import os
from socketserver import BaseRequestHandler, TCPServer

from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import AES

def serialise_cookie(cookie):
    fields = [f"{k}:{v}" for k, v in cookie.items()]
    return ",".join(fields).encode()

def deserialise_cookie(cookie_str):
    cookie = {}
    # strip off padding
    cookie_str = cookie_str[:cookie_str.find(b'\0')]
    for field in cookie_str.decode().split(","):
        k, v = field.split(":")
        try:
            cookie[k] = int(v)
        except ValueError:
            cookie[k] = v
    return cookie

class RequestHandler(BaseRequestHandler):
    def handle(self):
        key = os.urandom(16)
        cipher    = Cipher(AES(key), mode=modes.ECB())
        encryptor = cipher.encryptor()
        decryptor = cipher.decryptor()

        # generate session cookie containing user state
        cookie = serialise_cookie({
            "account":  "WebAdmin2",
            "timestamp": int(dt.datetime.now().timestamp()),
            "platform": "Win",
        })
        assert len(cookie) <= 64
        # encrypt session cookie with padding
        message = encryptor.update(cookie + b'\0' * (64 - len(cookie)))

        # send message to the client
        self.request.send(message)

        # receive and attempt to decode response
        try:
            message = decryptor.update(self.request.recv(64))
            cookie = deserialise_cookie(message)
            if cookie["account"] == "WebAdmin":
                self.request.send(b"flag{bu7_1m_3ncryp73d}")
                quit()
        except Exception as e:
            pass

TCPServer.allow_reuse_address = True
with TCPServer(("localhost", 8080), RequestHandler) as server:
    server.serve_forever()
