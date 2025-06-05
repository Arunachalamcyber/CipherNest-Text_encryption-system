from Crypto.Cipher import DES
import base64

def _pad(text: str) -> str:
    return text + (8 - len(text) % 8) * ' '

def encrypt_des(plain_text: str, key: str) -> str:
    key = key.ljust(8)[:8]
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    encrypted = cipher.encrypt(_pad(plain_text).encode())
    return base64.b64encode(encrypted).decode()

def decrypt_des(cipher_text: str, key: str) -> str:
    key = key.ljust(8)[:8]
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text.encode()))
    return decrypted.decode().strip()
