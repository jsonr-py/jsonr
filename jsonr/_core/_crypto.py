import hashlib
import hmac
import secrets

class Cryptography:
    def __init__(self):
        self.hashlib: object = hashlib
        self.hmac: object = hmac
        self.secrets: object = secrets
