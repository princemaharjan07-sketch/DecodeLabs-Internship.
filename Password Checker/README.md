# Password Strength Checker 🔐

**DecodeLabs Industrial Training Kit — Cyber Security Track**
**Project 1: Defensive Logic**

A simple Python program that evaluates whether a password is **Weak**, **Medium**, or **Strong** based on length and character variety.

## About

This project is the first milestone in the DecodeLabs Cyber Security internship track. Before working with hashing, encryption, or network defense, this project focuses on the fundamentals: **string handling**, **conditional logic**, and basic **security awareness** around what makes a password resistant to brute-force guessing.

## How It Works

The script checks a password against two categories of rules:

1. **Length** — the password must be at least 8 characters long.
2. **Character variety** — the password is checked for:
   - At least one number (`0-9`)
   - At least one symbol (e.g. `!@#$%^&*`)
   - At least one uppercase letter (`A-Z`)

Based on these checks, the password is classified as:

| Strength | Condition |
|----------|-----------|
| **Weak** | Under 8 characters, or 8+ characters but 0–1 variety checks passed |
| **Medium** | 8+ characters and 2 of the 3 variety checks passed |
| **Strong** | 8+ characters and all 3 variety checks passed |

## Getting Started

### Requirements
- Python 3.6 or later (no external libraries needed)

### Run it

```bash
python3 password_strength_checker.py
```

You'll be prompted to enter a password, and the program will print its strength.

### Example

```
=== Password Strength Checker ===
Enter a password to check: Abcdefg1!
Password Strength: Strong
```

## Example Results

| Password | Result | Why |
|----------|--------|-----|
| `abc` | Weak | Too short |
| `abcdefgh` | Weak | Long enough, but no number/symbol/uppercase |
| `Abcdefgh` | Weak | Only 1 of 3 variety checks (uppercase) |
| `Abcdefg1` | Medium | 2 of 3 variety checks (uppercase + number) |
| `Abcdefg1!` | Strong | All 3 variety checks passed |

## Skills Demonstrated

- Python string handling (`isdigit()`, `isupper()`, membership checks)
- Use of `any()` for efficient, short-circuiting condition checks
- Conditional logic for multi-tier classification
- Basic password security principles (length + entropy via character variety)

## What's Next

This is Project 1 in the DecodeLabs Cyber Security track. Project 2 builds on this foundation with **hashing and encryption**, using validated passwords as input.

---

*Built as part of the DecodeLabs Industrial Training Kit, Batch 2026.*
