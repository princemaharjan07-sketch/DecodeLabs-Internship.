# Caesar Cipher — Encryption & Decryption 🔒

**DecodeLabs Industrial Training Kit — Cyber Security Track**
**Project 2: Cryptographic Logic**

A Python implementation of the classic Caesar cipher, capable of both encrypting and decrypting text using a shift key.

## About

This is the second milestone in the DecodeLabs Cyber Security internship track. Where Project 1 focused on validating data, Project 2 shifts focus to **confidentiality** — protecting data in transit through mathematical transformation. The goal isn't "unbreakable" security (the Caesar cipher is intentionally simple), but mastering the core cryptographic building blocks: character-to-integer mapping, modular arithmetic, and reversible transformation logic that underpins every modern encryption algorithm, from Caesar to AES.

## How It Works

The Caesar cipher shifts each letter in the text forward by a fixed number of positions (the "key"), wrapping around the alphabet using modular arithmetic:

**Encryption:** `E(x) = (x + n) % 26`
**Decryption:** `D(x) = (x - n) % 26`

Where `x` is a letter's position in the alphabet (A=0, B=1, ... Z=25) and `n` is the shift key.

For example, with a shift of `3`:
- `A → D`
- `Y → B` (wraps around the alphabet)

The script converts each character to its numeric position using `ord()`, applies the shift, then converts back to a character using `chr()`. Non-letter characters (spaces, numbers, punctuation) are left unchanged.

## Getting Started

### Requirements
- Python 3.6 or later (no external libraries needed)

### Run it

```bash
python3 caesar_cipher.py
```

You'll be prompted for text to encrypt and a shift key. The program then prints the original, encrypted, and decrypted text so you can verify the round trip.

### Example

```
=== Caesar Cipher: Encryption & Decryption ===
Enter text to encrypt: Hello, World!
Enter shift key (e.g. 3): 3

Original text:  Hello, World!
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
```

## Example Results

| Input | Shift | Encrypted | Decrypted (verify) |
|-------|-------|-----------|---------------------|
| `HELLO` | 3 | `KHOOR` | `HELLO` |
| `attack at dawn` | 5 | `fyyfhp fy ifbs` | `attack at dawn` |
| `XYZ` | 3 | `ABC` | `XYZ` |

## Skills Demonstrated

- Character-to-integer conversion (`ord()`, `chr()`)
- Modular arithmetic for wrap-around logic (`% 26`)
- Symmetric encryption concepts (same key encrypts and decrypts)
- Edge-case handling (preserving spaces, digits, and punctuation)

## A Note on Security

The Caesar cipher is a teaching tool, not a real-world security solution. It has only 25 possible keys (trivial to brute-force) and preserves letter-frequency patterns, making it vulnerable to frequency analysis. Modern encryption (like AES) solves this through much larger key spaces and techniques like confusion and diffusion. This project is meant to build intuition for *how* encryption works before moving on to production-grade tools.

## What's Next

This is Project 2 in the DecodeLabs Cyber Security track, building directly on Project 1's password validation logic. Future milestones move toward stronger, real-world cryptographic techniques.

---

*Built as part of the DecodeLabs Industrial Training Kit, Batch 2026.*
