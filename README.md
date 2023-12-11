
# AES Implementation with Extended Key Lengths

## Introduction
This repository contains Python implementations of the Advanced Encryption Standard (AES) algorithm with various key lengths, including extended versions beyond the standard specifications. These implementations are purely for educational and research purposes and are not recommended for production use.

## Files in This Repository
- `AES_base.py`: The base implementation of AES, providing foundational functions used by all other scripts.
- `AES-128.py`: AES implementation with a 128-bit key.
- `AES-320.py`: Adapted AES implementation to support a 320-bit key.
- `AES-384.py`: Adapted AES implementation to support a 384-bit key.
- `AES-512.py`: Adapted AES implementation to support a 512-bit key.

## Installation
To use these scripts, ensure you have Python installed on your system. No additional libraries are required for the base implementation. However, for running advanced versions (AES-320, AES-384, and AES-512), the `numpy` library is needed.

Install numpy with pip:
```bash
pip install numpy
```

## Usage
Each script can be run independently. Here's an example of how to run the AES-128 implementation:
```bash
python AES-128.py
```

Replace `AES-128.py` with the desired script name to run different versions of AES.

## Implementation Details
- `AES_base.py` contains common functions like `sub_bytes`, `shift_rows`, `mix_columns`, and `add_round_key` used across all AES versions.
- `AES-128.py` is the standard AES implementation with a 128-bit key.
- `AES-320.py`, `AES-384.py`, and `AES-512.py` include modifications to the key expansion process and the number of encryption rounds to accommodate the respective key sizes.

## Testing
Each script includes a basic test case to demonstrate encryption. For comprehensive testing, use varied inputs and compare the outputs against known AES standards.

## Contributing
Contributions are welcome, especially for improving the implementations or adding more test cases. Please open a pull request with your contributions.

## Disclaimer
These implementations are for educational and research purposes only. They have not been thoroughly vetted for security and should not be used in production systems.

## Contact
For any queries or suggestions, please open an issue on the repository.
