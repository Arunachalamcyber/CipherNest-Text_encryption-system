from utils.banner import show_banner
from encryption import aes_cipher, des_cipher, rsa_cipher

def main():
    show_banner()

    print("Choose Algorithm:\n 1) AES\n 2) DES\n 3) RSA")
    algo = input(">> Select (1/2/3): ").strip()
    text = input(">> Enter text: ").strip()

    if algo == '1':
        key = input(">> Enter AES key (max 16 chars): ").strip()
        encrypted = aes_cipher.encrypt_aes(text, key)
        decrypted = aes_cipher.decrypt_aes(encrypted, key)
    elif algo == '2':
        key = input(">> Enter DES key (max 8 chars): ").strip()
        encrypted = des_cipher.encrypt_des(text, key)
        decrypted = des_cipher.decrypt_des(encrypted, key)
    elif algo == '3':
        pub_key, priv_key = rsa_cipher.generate_keys()
        encrypted = rsa_cipher.encrypt_rsa(text, pub_key)
        decrypted = rsa_cipher.decrypt_rsa(encrypted, priv_key)
    else:
        print("❌ Invalid Choice!")
        return

    print("\n🔐 Encrypted:", encrypted)
    print("🔓 Decrypted:", decrypted)
    print("✅ Operation Complete.")

if __name__ == "__main__":
    main()
