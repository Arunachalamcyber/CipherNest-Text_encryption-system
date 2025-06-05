from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

RSA_KEY_FILE = "keys/rsa_keys.pem"

def generate_keys():
    if not os.path.exists(RSA_KEY_FILE):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        os.makedirs("keys", exist_ok=True)
        with open(RSA_KEY_FILE, 'wb') as f:
            f.write(private_key + b'\n' + public_key)

    with open(RSA_KEY_FILE, 'rb') as f:
        keys = f.read().splitlines()
    private_key = RSA.import_key(keys[0])
    public_key = RSA.import_key(keys[1])
    return public_key, private_key

def encrypt_rsa(plain_text: str, pub_key) -> str:
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted = cipher.encrypt(plain_text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_rsa(cipher_text: str, priv_key) -> str:
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text.encode()))
    return decrypted.decode()
