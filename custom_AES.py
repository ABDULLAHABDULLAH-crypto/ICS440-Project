import numpy as np

from AES_version import AESVersion

BLOCK_SIZE = 4 # AES block size in words (AES uses 4x4 word blocks)
S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]


class CustomAES:
    def __init__(self, version: AESVersion):
        # Initialize AES with a specific version
        self.version = version
        self.Nk = version.value['Nk']
        self.Nr = version.value['Nr']
        self.Rcon = version.value['Rcon']

    def key_expansion(self, key):
        # Expand the cipher key into the key schedule for AES rounds
        def sub_word(word):
            # Substitute each byte in a word using the S-box
            return (S_BOX[word >> 24] << 24) | (S_BOX[(word >> 16) & 0xFF] << 16) | (S_BOX[(word >> 8) & 0xFF] << 8) | \
                S_BOX[word & 0xFF]

        def rot_word(word):
            # Rotate a word by 8 bits to the left
            return ((word << 8) & 0xFFFFFFFF) | (word >> 24)

        # Create an empty key schedule
        key_schedule = [0] * (BLOCK_SIZE * (self.Nr + 1))

        # Copy the initial key into the beginning of the key schedule
        for i in range(self.Nk):
            key_schedule[i] = (key[4 * i] << 24) | (key[4 * i + 1] << 16) | (key[4 * i + 2] << 8) | key[4 * i + 3]

        # Expand the key schedule
        for i in range(self.Nk, BLOCK_SIZE * (self.Nr + 1)):
            temp = key_schedule[i - 1]
            if i % self.Nk == 0:
                temp = sub_word(rot_word(temp)) ^ self.Rcon[i // self.Nk - 1]
            key_schedule[i] = key_schedule[i - self.Nk] ^ temp

        return key_schedule

    def encrypt(self, plaintext, key):
        if len(plaintext) % 16 != 0:
            raise ValueError("Plaintext must be a multiple of 16 bytes")

        # Initialize an empty string for the full ciphertext
        full_cipher_text = ""

        # Process each 16-byte (128-bit) block of the plaintext
        for block_start in range(0, len(plaintext), 16):
            # Extract the current block from plaintext
            block = plaintext[block_start:block_start + 16]
            # Convert the block to a state array
            state = np.array(list(block)).reshape((4, 4), order='F')
            # Get the round keys from the key expansion
            key_schedule = self.key_expansion(key)

            # Initial round
            state = add_round_key(state, key_schedule, 0)

            # Main rounds
            for i in range(1, self.Nr):
                state = sub_bytes(state)
                state = shift_rows(state)
                state = mix_columns(state)
                state = add_round_key(state, key_schedule, i)

            # Final round (no MixColumns)
            state = sub_bytes(state)
            state = shift_rows(state)
            state = add_round_key(state, key_schedule, self.Nr)

            # Convert the state to a hex string and append to the full ciphertext
            cipher_text_block = ""
            for i in range(4):  # Assuming the matrix is 4x4
                for row in state:
                    cipher_text_block += '{:02X}'.format(row[i])
            full_cipher_text += cipher_text_block

        return full_cipher_text


def sub_bytes(state):
    # Perform byte substitution using the S-box for each byte in the state
    for i in range(BLOCK_SIZE):
        for j in range(BLOCK_SIZE):
            state[i][j] = S_BOX[state[i][j]]
    return state


def shift_rows(state):
    # Copy each row of the state to a temporary list, shift it, and write it back
    for i in range(1, BLOCK_SIZE):
        row = state[i].tolist()  # Convert the numpy array row to a list
        state[i] = np.array(row[i:] + row[:i])  # Shift and convert back to numpy array
    return state


def xtime(a):
    # a function used for multiplying by {02} in GF(2^8).
    return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

# takes a column of the state matrix and mixes its bytes
def mix_single_column(column):
    # Multiply one column matrix
    t = column[0] ^ column[1] ^ column[2] ^ column[3]
    u = column[0]
    column[0] ^= t ^ xtime(column[0] ^ column[1])
    column[1] ^= t ^ xtime(column[1] ^ column[2])
    column[2] ^= t ^ xtime(column[2] ^ column[3])
    column[3] ^= t ^ xtime(column[3] ^ u)
    return column

# applies mix_single_column to each column of the state.
def mix_columns(state):
    for i in range(BLOCK_SIZE):
        column = [state[0][i], state[1][i], state[2][i], state[3][i]]
        column = mix_single_column(column)
        for j in range(BLOCK_SIZE):
            state[j][i] = column[j]
    return state

def add_round_key(state, key_schedule, round_num):
    for i in range(BLOCK_SIZE):
        # Extracting a word from the key schedule
        word = key_schedule[round_num * 4 + i]
        for j in range(BLOCK_SIZE):
            # Extracting the appropriate byte from the word
            key_byte = (word >> (8 * (3 - j))) & 0xFF
            state[j][i] ^= key_byte
    return state