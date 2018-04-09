"""Randomised One-Time Pad encryption and decryption functions in Python."""

import random

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    """Demo usage of functions."""
    vector = "Once more into the fray."
    encrypted = encrypt(vector)
    decrypted = decrypt(encrypted[0], encrypted[1])

    print("Test Vector: " + vector)
    print("OTP: " + encrypted[0])
    print("Encrypted: " + encrypted[1])
    print("Decrypted: " + decrypted)


def encrypt(plaintext):
    """Encrypt plaintext value.

    Keyword arguments:
    plaintext -- the plaintext value to encrypt.
    """
    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext.upper():
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]

    return otp, result


def decrypt(otp, secret):
    """Decrypt secret value.

    Keyword arguments:
    otp -- the one-time pad used when the secret value was encrypted.
    secret -- the value to be decrypted.
    """
    result = ""

    for c in secret.upper():
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]

    return result


if __name__ == "__main__":
    main()
