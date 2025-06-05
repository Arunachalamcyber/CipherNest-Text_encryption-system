from Crypto.Cipher import AES
import base64

# Padding to ensure block size match
def _pad(text: str) -> str:
    return text + (16 - len(text) % 16) * ' '

def encrypt_aes(plain_text: str, key: str) -> str:
    key = key.ljust(16)[:16]
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    encrypted = cipher.encrypt(_pad(plain_text).encode())
    return base64.b64encode(encrypted).decode()

def decrypt_aes(cipher_text: str, key: str) -> str:
    key = key.ljust(16)[:16]
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text.encode()))
    return decrypted.decode().strip()
