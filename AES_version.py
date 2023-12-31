from enum import Enum


class AESVersion(Enum):
    AES_128 = {'Nk': 4,  # Key length (in words)
               'Nr': 10,  # Number of rounds
               # Round constants table
               'Rcon': [
                   0x01000000, 0x02000000, 0x04000000, 0x08000000,
                   0x10000000, 0x20000000, 0x40000000, 0x80000000,
                   0x1B000000, 0x36000000,
               ]}
    AES_192 = {'Nk': 6,
               'Nr': 12,
               'Rcon': [
                   0x01000000, 0x02000000, 0x04000000, 0x08000000,
                   0x10000000, 0x20000000, 0x40000000, 0x80000000,
                   0x1B000000, 0x36000000, 0x6C000000, 0x36000000,
               ]}
    AES_256 = {'Nk': 8,
               'Nr': 14,
               'Rcon': [
                   0x01000000, 0x02000000, 0x04000000, 0x08000000,
                   0x10000000, 0x20000000, 0x40000000, 0x80000000,
                   0x1B000000, 0x36000000, 0x6C000000, 0x36000000,
                   0xAB000000, 0x4D000000,
               ]}
    AES_320 = {'Nk': 10,
               'Nr': 16,
               'Rcon': [
                   0x01000000, 0x02000000, 0x04000000, 0x08000000,
                   0x10000000, 0x20000000, 0x40000000, 0x80000000,
                   0x1B000000, 0x36000000, 0x6C000000, 0x36000000,
                   0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
               ]}
    AES_384 = {'Nk': 12,
               'Nr': 18,
               'Rcon': [
                   0x01000000, 0x02000000, 0x04000000, 0x08000000,
                   0x10000000, 0x20000000, 0x40000000, 0x80000000,
                   0x1B000000, 0x36000000, 0x6C000000, 0x36000000,
                   0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
                   0x5E000000, 0xBC000000,
               ]}
    AES_512 = {'Nk': 16,
               'Nr': 20,
               'Rcon': [
                   0x01000000, 0x02000000, 0x04000000, 0x08000000,
                   0x10000000, 0x20000000, 0x40000000, 0x80000000,
                   0x1B000000, 0x36000000, 0x6C000000, 0x36000000,
                   0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
                   0x5E000000, 0xBC000000, 0x63000000, 0xC6000000,
               ]}
