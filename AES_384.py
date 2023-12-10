import numpy as np
import AES_base as AES

Nk = 12
Nr = 18
Rcon = [
    0x01000000, 0x02000000, 0x04000000, 0x08000000,
    0x10000000, 0x20000000, 0x40000000, 0x80000000,
    0x1B000000, 0x36000000, 0x6C000000, 0xD8000000,
    0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
    0x5E000000, 0xBC000000
]

plaintext = b"\x00\x04\x12\x14\x12\x04\x12\x00\x0C\x00\x13\x11\x08\x23\x19\x19"
key = b"\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x13\xAA\x54\x87\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x13\xAA\x54\x87\x13\xAA\x54\x87\x13\xAA\x54\x87"
encrypted = AES.aes_encrypt(plaintext, key, Nk, Nr, Rcon)
print("Encrypted:", encrypted)
