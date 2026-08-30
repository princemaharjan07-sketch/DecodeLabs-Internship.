"""
DecodeLabs Industrial Training Kit — Cyber Security
Project 2: Basic Encryption & Decryption (Caesar Cipher)

Requirements (from brief):
    1. Encrypt user text using a basic logic (Caesar cipher or similar)
    2. Decrypt the encrypted text
    3. Display both encrypted and decrypted output

Math (from brief):
    Encryption: E_n(x) = (x + n) % 26
    Decryption: D_n(x) = (x - n) % 26
    where x = character position (A=0..Z=25), n = shift key

Skills: encryption concepts, logic building, data protection basics
"""

ALPHABET_SIZE = 26


def encrypt(text, shift):
    """
    Encrypts text using a Caesar cipher shift.
    Letters are shifted; spaces, numbers, and punctuation pass through unchanged
    (handles the 'edge cases' requirement from the brief).
    """
    result = []

    for char in text:
        if char.isupper():
            # Position relative to 'A' (65), apply shift, wrap with % 26, shift back
            shifted = (ord(char) - ord('A') + shift) % ALPHABET_SIZE
            result.append(chr(shifted + ord('A')))
        elif char.islower():
            # Position relative to 'a' (97), apply shift, wrap with % 26, shift back
            shifted = (ord(char) - ord('a') + shift) % ALPHABET_SIZE
            result.append(chr(shifted + ord('a')))
        else:
            # Spaces, digits, punctuation — leave untouched
            result.append(char)

    return "".join(result)


def decrypt(cipher_text, shift):
    """
    Decrypts text encrypted with the Caesar cipher by reversing the shift.
    This is the same logic as encrypt(), just with -shift.
    """
    return encrypt(cipher_text, -shift)


def main():
    print("=== Caesar Cipher: Encryption & Decryption ===")

    plaintext = input("Enter text to encrypt: ")

    while True:
        try:
            shift = int(input("Enter shift key (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a whole number.")

    encrypted = encrypt(plaintext, shift)
    decrypted = decrypt(encrypted, shift)

    print(f"\nOriginal text:  {plaintext}")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")


if __name__ == "__main__":
    main()
