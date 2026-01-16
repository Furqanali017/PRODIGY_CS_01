def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\nEncrypted Message:", encrypted_text)
    print("Decrypted Message:", decrypted_text)


if __name__ == "__main__":
    main()
